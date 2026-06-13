import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "v1-default")

@app.route('/')
def home():
    return jsonify({
        "service": "Secure Payment Gateway",
        "status": "online",
        "version": APP_VERSION
        })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
