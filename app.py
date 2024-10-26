from flask import Flask, render_template
from flask_cors import CORS  # You'll need to install this: pip install flask-cors

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Enable HTTPS if you want to access the camera on most browsers
    # You'll need to generate SSL certificates or use a service like ngrok
    app.run(host='0.0.0.0', port=5000, debug=True)