from flask import Flask, request
import logging
import sys

def create_app():
    app = Flask(__name__)

    # Configure logging to stdout (so GKE captures logs)
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

    logger = logging.getLogger(__name__)

    @app.after_request
    def after_request(response):
        """Log every response with proper severity based on status code."""
        status = response.status_code
        msg = f"{request.method} {request.path} {status}"

        if 200 <= status < 300:
            logger.info(msg)
        elif 400 <= status < 500:
            logger.warning(msg)
        elif 500 <= status < 600:
            logger.error(msg)
        else:
            logger.info(msg)

        return response

    from .main import register_routes
    register_routes(app)

    return app
