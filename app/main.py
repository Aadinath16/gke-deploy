from flask import Flask, render_template, jsonify
import logging
from datetime import datetime

app = Flask(__name__)

# Configure logging
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '{"timestamp": "%(asctime)s", "severity": "%(levelname)s", "message": "%(message)s", "logger": "%(name)s"}'
)
handler.setFormatter(formatter)
logger.addHandler(handler)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success")
def success():
    logger.info("Success endpoint hit (200)")
    return jsonify({"status": "success", "code": 200}), 200


@app.route("/error/400")
def bad_request():
    logger.warning("Client error simulated (400)")
    return jsonify({"status": "fail", "code": 400, "error": "Bad Request"}), 400


@app.route("/error/500")
def server_error():
    logger.error("Server error simulated (500)")
    return jsonify({"status": "fail", "code": 500, "error": "Internal Server Error"}), 500



# from flask import Flask, jsonify, abort, render_template
# import logging
# import sys
# from datetime import datetime

# app = Flask(__name__)

# # JSON formatter for structured logging
# class JsonFormatter(logging.Formatter):
#     def format(self, record):
#         log_record = {
#             "timestamp": datetime.utcnow().isoformat() + "Z",
#             "severity": record.levelname,
#             "message": record.getMessage(),
#             "logger": record.name,
#         }
#         return str(log_record).replace("'", '"')

# # Configure logging
# handler = logging.StreamHandler(sys.stdout)
# handler.setFormatter(JsonFormatter())
# logger = logging.getLogger("app")
# logger.setLevel(logging.INFO)
# logger.addHandler(handler)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/success")
# def success():
#     logger.info("Request handled successfully")
#     return jsonify({"message": "Success"}), 200

# @app.route("/error/400")
# def error_400():
#     abort(400)   # No logging here, handler will log

# @app.route("/error/500")
# def error_500():
#     abort(500)   # No logging here, handler will log

# # Error Handlers (only place where 4xx/5xx are logged)
# @app.errorhandler(400)
# def bad_request(error):
#     logger.warning("Client error occurred (400)")
#     return jsonify({"error": "Bad Request"}), 400

# @app.errorhandler(500)
# def internal_error(error):
#     logger.error("Server error occurred (500)")
#     return jsonify({"error": "Internal Server Error"}), 500

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)



# from flask import jsonify, render_template
# import logging

# logger = logging.getLogger(__name__)

# def register_routes(app):
#     @app.route("/")
#     def home():
#         return render_template("index.html")

#     @app.route("/ok")
#     def ok():
#         logger.info("200 OK response generated")
#         return jsonify({"message": "Everything is fine"}), 200

#     @app.route("/client-error")
#     def client_error():
#         logger.warning("Client error simulated (400)")
#         return jsonify({"error": "Bad Request"}), 400

#     @app.route("/server-error")
#     def server_error():
#         logger.error("Server error simulated (500)")
#         return jsonify({"error": "Internal Server Error"}), 500

#     @app.route("/status/<int:code>")
#     def custom_status(code):
#         if 200 <= code < 300:
#             logger.info(f"Custom {code} response")
#         elif 400 <= code < 500:
#             logger.warning(f"Custom {code} response")
#         elif 500 <= code < 600:
#             logger.error(f"Custom {code} response")
#         else:
#             logger.info(f"Unhandled {code} response")
#         return jsonify({"status": code}), code


#     @app.route("/external-test")
#     def external_test():
#         """Call an external API and log errors if it fails."""
#         try:
#             # Replace with your actual endpoint that may return 500
#             response = requests.get("http://example.com/api/trigger-500")
#             response.raise_for_status()  # Raises for 4xx/5xx
#             logger.info("External API call succeeded")
#             return jsonify({"message": "External call succeeded"}), 200
#         except requests.exceptions.HTTPError as e:
#             logger.error(f"External HTTP Error: {e.response.status_code} - {e.response.reason}")
#             return jsonify({"error": "External service failed"}), 500
#         except requests.exceptions.ConnectionError as e:
#             logger.error(f"External Connection Error: {e}")
#             return jsonify({"error": "Connection failed"}), 502