from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask on Vercel!"

@app.route('/api/endpoint')
def sample_endpoint():
    return {"message": "This is a sample API endpoint"}