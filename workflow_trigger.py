"""
Workflow Trigger for Button Analytics
This script triggers the Temporal workflow to analyze button performance
"""

import asyncio
import json
from datetime import datetime
from temporalio.client import Client
from temporal_workflows import ButtonAnalyticsWorkflow

async def trigger_button_analysis(property_id: str = "G-JHSVNWL6QH", days_back: int = 7):
    """Trigger the button analytics workflow"""
    
    print(f"🚀 Starting button analytics workflow for property: {property_id}")
    print(f"📅 Analyzing data from the last {days_back} days")
    
    try:
        # Connect to Temporal server
        client = await Client.connect("localhost:7233")
        
        # Start the workflow
        workflow_id = f"button-analytics-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        
        print(f"🔄 Starting workflow: {workflow_id}")
        
        # Execute the workflow
        result = await client.execute_workflow(
            ButtonAnalyticsWorkflow.run,
            args=[property_id, days_back],
            id=workflow_id,
            task_queue="button-analytics"
        )
        
        print("✅ Workflow completed successfully!")
        print(f"📊 Results: {json.dumps(result, indent=2, default=str)}")
        
        return result
        
    except Exception as e:
        print(f"❌ Error running workflow: {e}")
        return {"error": str(e)}

async def schedule_recurring_analysis(property_id: str = "G-JHSVNWL6QH"):
    """Schedule recurring button analysis (daily)"""
    
    print("⏰ Setting up recurring button analysis...")
    
    try:
        client = await Client.connect("localhost:7233")
        
        # Schedule daily analysis
        workflow_id = f"recurring-button-analysis-{datetime.now().strftime('%Y%m%d')}"
        
        # Start recurring workflow
        result = await client.execute_workflow(
            ButtonAnalyticsWorkflow.run,
            args=[property_id, 1],  # Analyze last 1 day
            id=workflow_id,
            task_queue="button-analytics"
        )
        
        print("✅ Recurring analysis scheduled!")
        return result
        
    except Exception as e:
        print(f"❌ Error scheduling recurring analysis: {e}")
        return {"error": str(e)}

def run_analysis_now():
    """Run analysis immediately (synchronous wrapper)"""
    return asyncio.run(trigger_button_analysis())

def schedule_daily_analysis():
    """Schedule daily analysis (synchronous wrapper)"""
    return asyncio.run(schedule_recurring_analysis())

if __name__ == "__main__":
    # Run immediate analysis
    print("🎯 Running immediate button analysis...")
    result = run_analysis_now()
    
    if "error" not in result:
        print("\n📈 Analysis completed! Check button_insights.json for detailed results.")
    else:
        print(f"\n❌ Analysis failed: {result['error']}")
