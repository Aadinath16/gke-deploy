# app/main.py
from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

# Use environment variable
APP_ENV = os.getenv("APP_ENV", "dev")

@app.route("/")
def home():
    return jsonify({
        "message": f"Hello from {APP_ENV} environment",
        "status": "success"
    }), 200  # Always success

@app.route("/random-status")
def random_status():
    """
    Returns a random status code:
      - 70% chance: 200 OK
      - 20% chance: 500 Internal Server Error
      - 10% chance: 404 Not Found
    """
    rnd = random.random()
    if rnd < 0.7:
        return jsonify({"message": "Everything is OK!", "status": "success"}), 200
    elif rnd < 0.9:
        return jsonify({"message": "Internal Server Error", "status": "error"}), 500
    else:
        return jsonify({"message": "Not Found", "status": "error"}), 404

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
