# app.py
from flask import Flask, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

@app.route('/')
def hello():
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content("Explain how AI works")
    print(response.text)
    return jsonify({"message": "Whatever!"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    # Note: When using UV, we use the CLI rather than this
    app.run(debug=True)

# Generated by Claude!