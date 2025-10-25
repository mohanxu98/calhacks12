from flask import Flask, render_template
import os

app = Flask(__name__)

# GA4 Configuration
GA4_MEASUREMENT_ID = os.environ.get('GA4_MEASUREMENT_ID', 'G-JHSVNWL6QH')  # Replace with your actual GA4 Measurement ID

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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)