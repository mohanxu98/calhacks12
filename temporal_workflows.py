"""
Temporal Workflows for GA4 Button Analytics Processing
This creates a DAG-like workflow to analyze button performance data
"""

import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from temporalio import workflow, activity
from temporalio.client import Client
import requests
import json

# Data structures for button analytics
@dataclass
class ButtonMetrics:
    button_id: str
    button_type: str
    page_variant: str
    total_clicks: int
    total_hovers: int
    avg_hover_duration: float
    click_through_rate: float
    engagement_score: float
    conversion_rate: float

@dataclass
class ButtonInsights:
    best_performing_button: str
    worst_performing_button: str
    most_engaging_variant: str
    button_recommendations: List[str]
    performance_summary: Dict[str, Any]

# Temporal Activities (individual tasks)
@activity.defn
async def fetch_ga4_data(property_id: str, start_date: str, end_date: str) -> Dict[str, Any]:
    """Fetch GA4 data from Google Analytics API"""
    # This would connect to GA4 Reporting API
    # For demo purposes, returning mock data structure
    return {
        "events": [
            {
                "event_name": "cta_click",
                "button_type": "cta",
                "page_variant": "original",
                "hover_duration": 1500,
                "total_engagement": 2000,
                "timestamp": "2024-01-01T10:00:00Z"
            },
            {
                "event_name": "navigation_click",
                "button_type": "navigation",
                "page_variant": "colors",
                "hover_duration": 800,
                "total_engagement": 1200,
                "timestamp": "2024-01-01T10:05:00Z"
            }
        ],
        "total_events": 150,
        "date_range": f"{start_date} to {end_date}"
    }

@activity.defn
async def process_button_metrics(raw_data: Dict[str, Any]) -> List[ButtonMetrics]:
    """Process raw GA4 data into button metrics"""
    events = raw_data.get("events", [])
    
    # Group events by button type and page variant
    button_groups = {}
    for event in events:
        key = f"{event.get('button_type', 'unknown')}_{event.get('page_variant', 'unknown')}"
        if key not in button_groups:
            button_groups[key] = {
                'clicks': 0,
                'hovers': 0,
                'hover_durations': [],
                'engagement_times': []
            }
        
        if event.get('event_name') in ['cta_click', 'navigation_click', 'feature_click']:
            button_groups[key]['clicks'] += 1
            button_groups[key]['engagement_times'].append(event.get('total_engagement', 0))
        
        if event.get('event_name') in ['button_hover_start', 'nav_hover_start', 'feature_hover_start']:
            button_groups[key]['hovers'] += 1
            button_groups[key]['hover_durations'].append(event.get('hover_duration', 0))
    
    # Calculate metrics for each button group
    metrics = []
    for key, data in button_groups.items():
        button_type, page_variant = key.split('_', 1)
        
        avg_hover_duration = sum(data['hover_durations']) / len(data['hover_durations']) if data['hover_durations'] else 0
        click_through_rate = data['clicks'] / data['hovers'] if data['hovers'] > 0 else 0
        avg_engagement = sum(data['engagement_times']) / len(data['engagement_times']) if data['engagement_times'] else 0
        
        # Calculate engagement score (combination of CTR, hover time, and clicks)
        engagement_score = (click_through_rate * 0.4 + 
                          (avg_hover_duration / 1000) * 0.3 + 
                          (data['clicks'] / 10) * 0.3)
        
        metrics.append(ButtonMetrics(
            button_id=key,
            button_type=button_type,
            page_variant=page_variant,
            total_clicks=data['clicks'],
            total_hovers=data['hovers'],
            avg_hover_duration=avg_hover_duration,
            click_through_rate=click_through_rate,
            engagement_score=engagement_score,
            conversion_rate=click_through_rate
        ))
    
    return metrics

@activity.defn
async def generate_button_insights(metrics: List[ButtonMetrics]) -> ButtonInsights:
    """Generate insights and recommendations from button metrics"""
    
    if not metrics:
        return ButtonInsights(
            best_performing_button="No data available",
            worst_performing_button="No data available",
            most_engaging_variant="No data available",
            button_recommendations=["Insufficient data for analysis"],
            performance_summary={}
        )
    
    # Find best and worst performing buttons
    best_button = max(metrics, key=lambda x: x.engagement_score)
    worst_button = min(metrics, key=lambda x: x.engagement_score)
    
    # Find most engaging page variant
    variant_scores = {}
    for metric in metrics:
        if metric.page_variant not in variant_scores:
            variant_scores[metric.page_variant] = []
        variant_scores[metric.page_variant].append(metric.engagement_score)
    
    most_engaging_variant = max(variant_scores.keys(), 
                               key=lambda x: sum(variant_scores[x]) / len(variant_scores[x]))
    
    # Generate recommendations
    recommendations = []
    
    if best_button.engagement_score > 0.7:
        recommendations.append(f"✅ {best_button.button_type} button on {best_button.page_variant} is performing excellently")
    
    if worst_button.engagement_score < 0.3:
        recommendations.append(f"⚠️ {worst_button.button_type} button on {worst_button.page_variant} needs improvement")
    
    if best_button.avg_hover_duration > 2000:
        recommendations.append("💡 Consider making buttons more prominent - users are hovering for a long time")
    
    if best_button.click_through_rate < 0.5:
        recommendations.append("🎯 Focus on improving button visibility and call-to-action clarity")
    
    # Performance summary
    performance_summary = {
        "total_buttons_analyzed": len(metrics),
        "average_engagement_score": sum(m.engagement_score for m in metrics) / len(metrics),
        "best_engagement_score": best_button.engagement_score,
        "worst_engagement_score": worst_button.engagement_score,
        "most_clicked_button": max(metrics, key=lambda x: x.total_clicks).button_id,
        "highest_ctr_button": max(metrics, key=lambda x: x.click_through_rate).button_id
    }
    
    return ButtonInsights(
        best_performing_button=f"{best_button.button_type} on {best_button.page_variant}",
        worst_performing_button=f"{worst_button.button_type} on {worst_button.page_variant}",
        most_engaging_variant=most_engaging_variant,
        button_recommendations=recommendations,
        performance_summary=performance_summary
    )

@activity.defn
async def save_insights_to_database(insights: ButtonInsights) -> str:
    """Save insights to database or file"""
    # In a real implementation, this would save to a database
    # For demo, saving to a JSON file
    insights_data = {
        "timestamp": datetime.now().isoformat(),
        "best_performing_button": insights.best_performing_button,
        "worst_performing_button": insights.worst_performing_button,
        "most_engaging_variant": insights.most_engaging_variant,
        "recommendations": insights.button_recommendations,
        "performance_summary": insights.performance_summary
    }
    
    with open("button_insights.json", "w") as f:
        json.dump(insights_data, f, indent=2)
    
    return f"Insights saved to button_insights.json at {datetime.now()}"

@activity.defn
async def send_insights_notification(insights: ButtonInsights) -> str:
    """Send insights via email, Slack, or other notification system"""
    # This would integrate with your notification system
    message = f"""
    🎯 Button Analytics Report
    
    Best Performing Button: {insights.best_performing_button}
    Worst Performing Button: {insights.worst_performing_button}
    Most Engaging Variant: {insights.most_engaging_variant}
    
    Recommendations:
    {chr(10).join(f"• {rec}" for rec in insights.button_recommendations)}
    """
    
    print(f"📧 Notification sent: {message}")
    return f"Notification sent at {datetime.now()}"

# Temporal Workflow (DAG-like orchestration)
@workflow.defn
class ButtonAnalyticsWorkflow:
    """Main workflow for processing GA4 button analytics"""
    
    @workflow.run
    async def run(self, property_id: str, days_back: int = 7) -> Dict[str, Any]:
        """Main workflow execution"""
        
        # Calculate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days_back)
        
        # Step 1: Fetch GA4 data
        workflow.logger.info("🔄 Fetching GA4 data...")
        raw_data = await workflow.execute_activity(
            fetch_ga4_data,
            args=[property_id, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")],
            start_to_close_timeout=timedelta(minutes=5)
        )
        
        # Step 2: Process button metrics
        workflow.logger.info("📊 Processing button metrics...")
        metrics = await workflow.execute_activity(
            process_button_metrics,
            args=[raw_data],
            start_to_close_timeout=timedelta(minutes=3)
        )
        
        # Step 3: Generate insights
        workflow.logger.info("🧠 Generating insights...")
        insights = await workflow.execute_activity(
            generate_button_insights,
            args=[metrics],
            start_to_close_timeout=timedelta(minutes=2)
        )
        
        # Step 4: Save insights (parallel with notification)
        workflow.logger.info("💾 Saving insights...")
        save_task = workflow.execute_activity(
            save_insights_to_database,
            args=[insights],
            start_to_close_timeout=timedelta(minutes=1)
        )
        
        # Step 5: Send notification (parallel with save)
        workflow.logger.info("📧 Sending notification...")
        notify_task = workflow.execute_activity(
            send_insights_notification,
            args=[insights],
            start_to_close_timeout=timedelta(minutes=1)
        )
        
        # Wait for both parallel tasks to complete
        save_result, notify_result = await asyncio.gather(save_task, notify_task)
        
        # Return workflow results
        return {
            "status": "completed",
            "timestamp": datetime.now().isoformat(),
            "data_points_processed": raw_data.get("total_events", 0),
            "buttons_analyzed": len(metrics),
            "best_button": insights.best_performing_button,
            "recommendations_count": len(insights.button_recommendations),
            "save_result": save_result,
            "notification_result": notify_result
        }

# Workflow execution function
async def run_button_analytics_workflow(property_id: str, days_back: int = 7):
    """Execute the button analytics workflow"""
    
    # Connect to Temporal server
    client = await Client.connect("localhost:7233")
    
    # Start the workflow
    workflow_id = f"button-analytics-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    
    result = await client.execute_workflow(
        ButtonAnalyticsWorkflow.run,
        args=[property_id, days_back],
        id=workflow_id,
        task_queue="button-analytics"
    )
    
    return result

# Example usage
if __name__ == "__main__":
    # Run the workflow
    asyncio.run(run_button_analytics_workflow("G-JHSVNWL6QH", days_back=7))
