from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='../templates')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

# This is important for Vercel
if __name__ == '__main__':
    app.run()