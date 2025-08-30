from flask import Flask
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

    from .main import register_routes
    register_routes(app)

    return app
