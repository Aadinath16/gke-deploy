from flask import Flask, jsonify
import os
import random
import logging

app = Flask(__name__)

# Structured logging (for Cloud Logging parsing)
logging.basicConfig(level=logging.INFO, format="%(message)s")

# Environment variables (from GKE ConfigMap/Secret)
APP_ENV = os.getenv("APP_ENV", "dev")              # from ConfigMap
SECRET_KEY = os.getenv("SECRET_KEY", "changeme")  # from Secret


@app.route("/")
def home():
    app.logger.info({
        "event": "home",
        "status": 200,
        "environment": APP_ENV
    })
    return jsonify({
        "message": "Hello from Flask app on GKE!",
        "environment": APP_ENV,
        "secret_key": SECRET_KEY  # ⚠️ demo only (don’t log secrets in prod)
    }), 200


@app.route("/success")
def success():
    app.logger.info({"event": "success", "status": 200})
    return jsonify({"status": "Success", "code": 200}), 200


@app.route("/client-error")
def client_error():
    errors = [
        (400, "Bad Request"),
        (401, "Unauthorized"),
        (403, "Forbidden"),
        (404, "Not Found")
    ]
    code, msg = random.choice(errors)
    app.logger.warning({"event": "client-error", "status": code, "message": msg})
    return jsonify({"error": msg, "code": code}), code


@app.route("/server-error")
def server_error():
    errors = [
        (500, "Internal Server Error"),
        (502, "Bad Gateway"),
        (503, "Service Unavailable")
    ]
    code, msg = random.choice(errors)
    app.logger.error({"event": "server-error", "status": code, "message": msg})
    return jsonify({"error": msg, "code": code}), code


@app.route("/random")
def random_status():
    """Randomly return 2xx, 4xx, or 5xx"""
    routes = [success, client_error, server_error]
    return random.choice(routes)()


if __name__ == "__main__":
    # Run Flask dev server (for local debugging)
    app.run(host="0.0.0.0", port=8080, debug=True)
