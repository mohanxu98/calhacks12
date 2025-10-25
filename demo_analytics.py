"""
Demo script that shows the analytics system working
This runs the workflow without requiring Temporal server
"""

import asyncio
import json
from temporal_workflows import (
    fetch_ga4_data,
    process_button_metrics,
    generate_button_insights,
    save_insights_to_database,
    send_insights_notification
)

async def run_demo_analysis():
    """Run a complete demo of the button analytics workflow"""
    
    print("🎯 Button Analytics Demo")
    print("=" * 50)
    
    # Step 1: Fetch GA4 data
    print("\n📊 Step 1: Fetching GA4 data...")
    raw_data = await fetch_ga4_data("G-JHSVNWL6QH", "2024-01-01", "2024-01-08")
    print(f"✅ Fetched {len(raw_data.get('events', []))} events from GA4")
    
    # Step 2: Process button metrics
    print("\n⚙️ Step 2: Processing button metrics...")
    metrics = await process_button_metrics(raw_data)
    print(f"✅ Processed {len(metrics)} button groups")
    
    for metric in metrics:
        print(f"   📈 {metric.button_type} on {metric.page_variant}:")
        print(f"      - Clicks: {metric.total_clicks}")
        print(f"      - Hovers: {metric.total_hovers}")
        print(f"      - Avg hover duration: {metric.avg_hover_duration:.0f}ms")
        print(f"      - Click-through rate: {metric.click_through_rate:.2%}")
        print(f"      - Engagement score: {metric.engagement_score:.2f}")
    
    # Step 3: Generate insights
    print("\n🧠 Step 3: Generating insights...")
    insights = await generate_button_insights(metrics)
    
    print(f"✅ Insights generated:")
    print(f"   🏆 Best performing button: {insights.best_performing_button}")
    print(f"   ⚠️ Worst performing button: {insights.worst_performing_button}")
    print(f"   🎯 Most engaging variant: {insights.most_engaging_variant}")
    
    print(f"\n💡 Recommendations:")
    for i, rec in enumerate(insights.button_recommendations, 1):
        print(f"   {i}. {rec}")
    
    # Step 4: Save insights
    print(f"\n💾 Step 4: Saving insights...")
    save_result = await save_insights_to_database(insights)
    print(f"✅ {save_result}")
    
    # Step 5: Send notification
    print(f"\n📧 Step 5: Sending notification...")
    notify_result = await send_insights_notification(insights)
    print(f"✅ {notify_result}")
    
    # Show performance summary
    print(f"\n📈 Performance Summary:")
    summary = insights.performance_summary
    print(f"   - Total buttons analyzed: {summary['total_buttons_analyzed']}")
    print(f"   - Average engagement score: {summary['average_engagement_score']:.2f}")
    print(f"   - Best engagement score: {summary['best_engagement_score']:.2f}")
    print(f"   - Most clicked button: {summary['most_clicked_button']}")
    print(f"   - Highest CTR button: {summary['highest_ctr_button']}")
    
    print(f"\n🎉 Demo completed successfully!")
    print(f"\n📋 Next steps:")
    print(f"1. Visit http://localhost:5001/analytics for the dashboard")
    print(f"2. Check button_insights.json for detailed results")
    print(f"3. Set up Temporal server for production workflows")
    
    return insights

def show_insights_file():
    """Show the contents of the generated insights file"""
    try:
        with open('button_insights.json', 'r') as f:
            insights = json.load(f)
        
        print(f"\n📄 Generated Insights File (button_insights.json):")
        print("=" * 50)
        print(json.dumps(insights, indent=2, default=str))
        
    except FileNotFoundError:
        print("❌ Insights file not found")

async def main():
    """Run the complete demo"""
    # Run the analysis
    insights = await run_demo_analysis()
    
    # Show the generated file
    show_insights_file()

if __name__ == "__main__":
    asyncio.run(main())
