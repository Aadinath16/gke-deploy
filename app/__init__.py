from flask import Flask
import logging
from google.cloud import logging as gcp_logging
from flask import request

def create_app():
    app = Flask(__name__)

    # Initialize GCP Logging
    client = gcp_logging.Client()
    client.setup_logging()

    # Set Flask logger to use GCP logging
    handler = logging.getLogger('werkzeug')
    handler.setLevel(logging.INFO)

    # Import routes
    from app.main import main_bp
    app.register_blueprint(main_bp)

    # Log based on response code
    @app.after_request
    def after_request(response):
        status_code = response.status_code
        if 200 <= status_code < 300:
            app.logger.info(f"{request.method} {request.path} {status_code}")
        elif 400 <= status_code < 500:
            app.logger.warning(f"{request.method} {request.path} {status_code}")
        elif 500 <= status_code < 600:
            app.logger.error(f"{request.method} {request.path} {status_code}")
        return response

    return app
