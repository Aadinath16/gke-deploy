import logging
from flask import Flask, jsonify
import random, os

app = Flask(__name__)

# Configure logging
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '[%(asctime)s] [%(levelname)s] %(message)s'
)
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

APP_ENV = os.getenv("APP_ENV", "dev")

@app.route("/")
def home():
    app.logger.info("200 OK response for /")
    return jsonify({"message": f"Hello from {APP_ENV}", "status": "success"}), 200

@app.route("/random-status")
def random_status():
    rnd = random.random()
    if rnd < 0.7:
        app.logger.info("200 OK response for /random-status")
        return jsonify({"message": "Everything OK!", "status": "success"}), 200
    elif rnd < 0.9:
        app.logger.error("500 Internal Server Error simulated")
        return jsonify({"message": "Internal Server Error", "status": "error"}), 500
    else:
        app.logger.warning("404 Not Found simulated")
        return jsonify({"message": "Not Found", "status": "error"}), 404

@app.route("/health")
def health():
    app.logger.info("Health check OK")
    return jsonify({"status": "healthy"}), 200
