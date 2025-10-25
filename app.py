from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/colors')
def colors():
    return render_template('colors.html')

@app.route('/sizes')
def sizes():
    return render_template('sizes.html')

@app.route('/spacing')
def spacing():
    return render_template('spacing.html')

@app.route('/typography')
def typography():
    return render_template('typography.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)