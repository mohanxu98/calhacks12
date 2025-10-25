"""
Test script for the analytics system
This tests the workflow without requiring Temporal server
"""

import json
from temporal_workflows import (
    fetch_ga4_data,
    process_button_metrics,
    generate_button_insights,
    save_insights_to_database,
    send_insights_notification
)

async def test_workflow_components():
    """Test individual workflow components"""
    print("🧪 Testing Temporal workflow components...")
    
    # Test 1: Fetch GA4 data (mock)
    print("\n1️⃣ Testing GA4 data fetch...")
    try:
        raw_data = await fetch_ga4_data("G-JHSVNWL6QH", "2024-01-01", "2024-01-08")
        print(f"✅ GA4 data fetched: {len(raw_data.get('events', []))} events")
    except Exception as e:
        print(f"❌ GA4 data fetch failed: {e}")
        return False
    
    # Test 2: Process button metrics
    print("\n2️⃣ Testing button metrics processing...")
    try:
        metrics = await process_button_metrics(raw_data)
        print(f"✅ Button metrics processed: {len(metrics)} button groups")
        for metric in metrics:
            print(f"   - {metric.button_type} on {metric.page_variant}: {metric.total_clicks} clicks, {metric.engagement_score:.2f} score")
    except Exception as e:
        print(f"❌ Button metrics processing failed: {e}")
        return False
    
    # Test 3: Generate insights
    print("\n3️⃣ Testing insights generation...")
    try:
        insights = await generate_button_insights(metrics)
        print(f"✅ Insights generated:")
        print(f"   - Best button: {insights.best_performing_button}")
        print(f"   - Worst button: {insights.worst_performing_button}")
        print(f"   - Best variant: {insights.most_engaging_variant}")
        print(f"   - Recommendations: {len(insights.button_recommendations)}")
    except Exception as e:
        print(f"❌ Insights generation failed: {e}")
        return False
    
    # Test 4: Save insights
    print("\n4️⃣ Testing insights saving...")
    try:
        save_result = await save_insights_to_database(insights)
        print(f"✅ Insights saved: {save_result}")
    except Exception as e:
        print(f"❌ Insights saving failed: {e}")
        return False
    
    # Test 5: Send notification
    print("\n5️⃣ Testing notification sending...")
    try:
        notify_result = await send_insights_notification(insights)
        print(f"✅ Notification sent: {notify_result}")
    except Exception as e:
        print(f"❌ Notification sending failed: {e}")
        return False
    
    return True

def test_flask_endpoints():
    """Test Flask app endpoints"""
    print("\n🌐 Testing Flask endpoints...")
    
    try:
        from app import app
        
        with app.test_client() as client:
            # Test analytics dashboard
            response = client.get('/analytics')
            if response.status_code == 200:
                print("✅ Analytics dashboard accessible")
            else:
                print(f"❌ Analytics dashboard failed: {response.status_code}")
            
            # Test button insights API
            response = client.get('/api/button-insights')
            if response.status_code in [200, 404]:  # 404 is expected if no data yet
                print("✅ Button insights API working")
            else:
                print(f"❌ Button insights API failed: {response.status_code}")
                
    except Exception as e:
        print(f"❌ Flask endpoints test failed: {e}")
        return False
    
    return True

async def main():
    """Run all tests"""
    print("🎯 Testing Temporal Workflow System for Button Analytics")
    print("=" * 60)
    
    # Test workflow components
    workflow_success = await test_workflow_components()
    
    # Test Flask endpoints
    flask_success = test_flask_endpoints()
    
    print("\n" + "=" * 60)
    print("📊 Test Results:")
    print(f"✅ Workflow Components: {'PASS' if workflow_success else 'FAIL'}")
    print(f"✅ Flask Endpoints: {'PASS' if flask_success else 'FAIL'}")
    
    if workflow_success and flask_success:
        print("\n🎉 All tests passed! Your Temporal workflow system is ready!")
        print("\n📋 Next steps:")
        print("1. Start Temporal server: temporal server start-dev")
        print("2. Start worker: python temporal_worker.py")
        print("3. Visit: http://localhost:5001/analytics")
        print("4. Click 'Run Button Analysis' to test the workflow")
    else:
        print("\n❌ Some tests failed. Check the errors above.")
    
    return workflow_success and flask_success

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
