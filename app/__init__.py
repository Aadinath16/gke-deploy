from flask import Flask, request
import logging
import sys
import json
from datetime import datetime

class GCPJsonFormatter(logging.Formatter):
    """Format logs as JSON with severity for GCP Log Explorer"""
    def format(self, record):
        log_obj = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "severity": record.levelname,
            "message": record.getMessage(),
            "logger": record.name,
        }
        return json.dumps(log_obj)

def create_app():
    app = Flask(__name__)

    # Configure JSON logging
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(GCPJsonFormatter())
    root = logging.getLogger()
    root.handlers = [handler]
    root.setLevel(logging.INFO)

    logger = logging.getLogger(__name__)

    @app.after_request
    def after_request(response):
        """Log every response with correct severity and structured fields"""
        status = response.status_code
        log_obj = {
            "httpRequest": {
                "requestMethod": request.method,
                "requestUrl": request.path,
                "status": status,
                "userAgent": request.headers.get("User-Agent"),
                "remoteIp": request.remote_addr,
            }
        }

        if 200 <= status < 300:
            logger.info(f"Request handled successfully", extra=log_obj)
        elif 400 <= status < 500:
            logger.warning(f"Client error occurred", extra=log_obj)
        elif 500 <= status < 600:
            logger.error(f"Server error occurred", extra=log_obj)
        else:
            logger.info(f"Other response", extra=log_obj)

        return response

    from .main import register_routes
    register_routes(app)

    return app
