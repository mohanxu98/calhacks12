from flask import Flask, render_template, jsonify, request
import os
import asyncio
from workflow_trigger import trigger_button_analysis

app = Flask(__name__)

# GA4 Configuration
GA4_MEASUREMENT_ID = os.environ.get('GA4_MEASUREMENT_ID', 'G-JHSVNWL6QH')  

@app.route('/')
def home():
    return render_template('index.html', 
                          ga4_measurement_id=GA4_MEASUREMENT_ID,
                          page_variant='original')

@app.route('/colors')
def colors():
    return render_template('colors.html', 
                          ga4_measurement_id=GA4_MEASUREMENT_ID,
                          page_variant='colors')

@app.route('/sizes')
def sizes():
    return render_template('sizes.html', 
                          ga4_measurement_id=GA4_MEASUREMENT_ID,
                          page_variant='sizes')

@app.route('/spacing')
def spacing():
    return render_template('spacing.html', 
                          ga4_measurement_id=GA4_MEASUREMENT_ID,
                          page_variant='spacing')

@app.route('/typography')
def typography():
    return render_template('typography.html', 
                          ga4_measurement_id=GA4_MEASUREMENT_ID,
                          page_variant='typography')

# Temporal Workflow Endpoints
@app.route('/api/analyze-buttons', methods=['POST'])
def analyze_buttons():
    """Trigger button analytics workflow"""
    try:
        days_back = request.json.get('days_back', 7) if request.is_json else 7
        
        # Run the workflow asynchronously
        result = asyncio.run(trigger_button_analysis(GA4_MEASUREMENT_ID, days_back))
        
        return jsonify({
            'status': 'success',
            'message': 'Button analysis workflow started',
            'workflow_id': result.get('workflow_id', 'unknown'),
            'results': result
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Failed to start workflow: {str(e)}'
        }), 500

@app.route('/api/button-insights', methods=['GET'])
def get_button_insights():
    """Get latest button insights from analysis"""
    try:
        import json
        with open('button_insights.json', 'r') as f:
            insights = json.load(f)
        return jsonify(insights)
    except FileNotFoundError:
        return jsonify({
            'status': 'no_data',
            'message': 'No button insights available yet. Run analysis first.'
        }), 404
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Failed to load insights: {str(e)}'
        }), 500

@app.route('/analytics')
def analytics_dashboard():
    """Analytics dashboard page"""
    return render_template('analytics.html', 
                          ga4_measurement_id=GA4_MEASUREMENT_ID,
                          page_variant='analytics')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)