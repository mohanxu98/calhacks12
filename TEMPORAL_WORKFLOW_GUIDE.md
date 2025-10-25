# Temporal Workflow System for Button Analytics

## 🎯 Overview
This system uses Temporal to create a DAG-like workflow that processes Google Analytics 4 (GA4) button interaction data and generates actionable insights about button performance.

## 🔄 Workflow Architecture

### **DAG Structure:**
```
GA4 Data Fetch → Process Metrics → Generate Insights → [Save Insights + Send Notifications]
                                                      ↓
                                              Parallel Execution
```

### **Workflow Steps:**

1. **📊 Fetch GA4 Data** (`fetch_ga4_data`)
   - Connects to Google Analytics 4 API
   - Retrieves button interaction events
   - Returns structured data for processing

2. **⚙️ Process Button Metrics** (`process_button_metrics`)
   - Calculates engagement scores
   - Computes click-through rates
   - Analyzes hover durations
   - Groups data by button type and page variant

3. **🧠 Generate Insights** (`generate_button_insights`)
   - Identifies best/worst performing buttons
   - Finds most engaging page variants
   - Creates actionable recommendations
   - Generates performance summaries

4. **💾 Save & Notify** (Parallel execution)
   - **Save Insights** (`save_insights_to_database`)
   - **Send Notifications** (`send_insights_notification`)

## 🚀 Quick Start

### **1. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **2. Set Up Temporal Server**
```bash
# Install Temporal CLI
brew install temporalio/tap/temporal  # macOS
# or
curl -sSf https://temporal.download/cli.sh | sh  # Linux

# Start Temporal server
temporal server start-dev
```

### **3. Start the Worker**
```bash
python temporal_worker.py
```

### **4. Run Your Flask App**
```bash
python app.py
```

### **5. Access Analytics Dashboard**
Visit: **http://localhost:5001/analytics**

## 📊 Analytics Dashboard Features

### **Button Performance Insights:**
- **Best Performing Button** - Highest engagement score
- **Worst Performing Button** - Needs improvement
- **Most Engaging Variant** - Best page design
- **Actionable Recommendations** - Specific improvements

### **Metrics Tracked:**
- **Click-through rates** by button type
- **Hover durations** and engagement patterns
- **Button performance** across page variants
- **User interaction sequences**

## 🔧 API Endpoints

### **Trigger Analysis:**
```bash
POST /api/analyze-buttons
Content-Type: application/json

{
  "days_back": 7
}
```

### **Get Insights:**
```bash
GET /api/button-insights
```

## 📈 Workflow Benefits

### **1. Automated Analysis**
- Runs automatically based on GA4 data
- Processes large datasets efficiently
- Generates insights without manual intervention

### **2. Scalable Processing**
- Handles multiple button types simultaneously
- Processes data across all page variants
- Scales with your user base

### **3. Actionable Insights**
- Identifies which buttons work best
- Suggests specific improvements
- Compares performance across designs

### **4. Real-time Monitoring**
- Temporal UI shows workflow progress
- Real-time status updates
- Error handling and retries

## 🎯 Use Cases

### **A/B Testing Analysis:**
- Compare button performance across page variants
- Identify winning designs
- Optimize user experience

### **Button Optimization:**
- Find underperforming buttons
- Improve call-to-action effectiveness
- Enhance user engagement

### **Performance Monitoring:**
- Track button engagement trends
- Monitor user behavior changes
- Generate regular reports

## 🔍 Workflow Execution

### **Manual Trigger:**
```python
from workflow_trigger import trigger_button_analysis

# Run analysis for last 7 days
result = trigger_button_analysis("G-JHSVNWL6QH", days_back=7)
```

### **Scheduled Analysis:**
```python
from workflow_trigger import schedule_daily_analysis

# Schedule daily analysis
schedule_daily_analysis()
```

## 📊 Output Examples

### **Button Insights JSON:**
```json
{
  "timestamp": "2024-01-01T10:00:00Z",
  "best_performing_button": "cta on original",
  "worst_performing_button": "navigation on typography",
  "most_engaging_variant": "colors",
  "recommendations": [
    "✅ cta button on original is performing excellently",
    "⚠️ navigation button on typography needs improvement",
    "💡 Consider making buttons more prominent"
  ],
  "performance_summary": {
    "total_buttons_analyzed": 15,
    "average_engagement_score": 0.65,
    "most_clicked_button": "cta_original"
  }
}
```

## 🛠️ Customization

### **Add New Metrics:**
```python
# In process_button_metrics activity
def calculate_custom_metric(events):
    # Your custom calculation
    return custom_value
```

### **Custom Notifications:**
```python
# In send_insights_notification activity
async def send_slack_notification(insights):
    # Send to Slack
    pass
```

### **Additional Data Sources:**
```python
# Add new data sources
@activity.defn
async def fetch_additional_data():
    # Fetch from other analytics tools
    pass
```

## 🔧 Troubleshooting

### **Temporal Server Issues:**
```bash
# Check server status
temporal server start-dev --log-level debug

# Reset server
temporal server start-dev --headless
```

### **Worker Connection Issues:**
```bash
# Check worker logs
python temporal_worker.py --log-level debug
```

### **Workflow Failures:**
- Check Temporal UI at http://localhost:8080
- Review workflow execution history
- Check error logs in worker output

## 📚 Next Steps

1. **Set up real GA4 API integration**
2. **Add more sophisticated metrics**
3. **Implement machine learning insights**
4. **Create automated optimization workflows**
5. **Add real-time alerting**

Your Temporal workflow system is now ready to process GA4 button analytics and generate actionable insights! 🎉
