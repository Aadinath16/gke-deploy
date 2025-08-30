from flask import jsonify, render_template
import logging

logger = logging.getLogger(__name__)

def register_routes(app):
    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/ok")
    def ok():
        logger.info("200 OK response generated")
        return jsonify({"message": "Everything is fine"}), 200

    @app.route("/client-error")
    def client_error():
        logger.warning("Client error simulated (400)")
        return jsonify({"error": "Bad Request"}), 400

    @app.route("/server-error")
    def server_error():
        logger.error("Server error simulated (500)")
        return jsonify({"error": "Internal Server Error"}), 500

    @app.route("/status/<int:code>")
    def custom_status(code):
        if 200 <= code < 300:
            logger.info(f"Custom {code} response")
        elif 400 <= code < 500:
            logger.warning(f"Custom {code} response")
        elif 500 <= code < 600:
            logger.error(f"Custom {code} response")
        else:
            logger.info(f"Unhandled {code} response")
        return jsonify({"status": code}), code
