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


    @app.route("/external-test")
    def external_test():
        """Call an external API and log errors if it fails."""
        try:
            # Replace with your actual endpoint that may return 500
            response = requests.get("http://example.com/api/trigger-500")
            response.raise_for_status()  # Raises for 4xx/5xx
            logger.info("External API call succeeded")
            return jsonify({"message": "External call succeeded"}), 200
        except requests.exceptions.HTTPError as e:
            logger.error(f"External HTTP Error: {e.response.status_code} - {e.response.reason}")
            return jsonify({"error": "External service failed"}), 500
        except requests.exceptions.ConnectionError as e:
            logger.error(f"External Connection Error: {e}")
            return jsonify({"error": "Connection failed"}), 502