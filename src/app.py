"""
Truth Lens - Application Factory and Server Entry Point.

Initializes the web application, sets up static routing, blueprints,
health checks, and error handlers.
"""

from pathlib import Path
from flask import Flask, jsonify, send_from_directory
from src.config.settings import get_settings
from src.utils.logger import get_logger
from src.utils.helpers import json_response
from src.pages.routes import pages_bp


def create_app() -> Flask:
    """
    Constructs and configures the Flask application instance.
    """
    settings = get_settings()
    logger = get_logger("truth_lens.app")

    app = Flask(
        __name__,
        static_folder=str(settings.PUBLIC_DIR),
        static_url_path=""
    )

    # Core configuration
    app.config["SECRET_KEY"] = settings.SECRET_KEY
    app.config["ENV"] = settings.APP_ENV
    app.config["DEBUG"] = settings.DEBUG

    # Register modular blueprints
    app.register_blueprint(pages_bp)

    # Core Foundation API: Health Check
    @app.route("/api/health", methods=["GET"])
    def health_check():
        """System health and heartbeat check."""
        return jsonify(
            json_response(
                data={
                    "status": "operational",
                    "app_name": settings.APP_NAME,
                    "environment": settings.APP_ENV,
                    "debug": settings.DEBUG,
                    "foundation": "ready"
                },
                message="Truth Lens core services healthy"
            )
        ), 200

    # Static file direct routing fallback for public folder assets
    @app.route("/assets/<path:filename>")
    def custom_assets(filename):
        assets_dir = settings.PUBLIC_DIR / "assets"
        return send_from_directory(assets_dir, filename)

    @app.route("/images/<path:filename>")
    def custom_images(filename):
        images_dir = settings.PUBLIC_DIR / "images"
        return send_from_directory(images_dir, filename)

    # Error handling
    @app.errorhandler(404)
    def not_found(error):
        return jsonify(
            json_response(
                data={"error": "Not Found", "details": str(error)},
                status_code=404,
                message="Requested resource not found",
                success=False
            )
        ), 404

    @app.errorhandler(500)
    def internal_error(error):
        logger.error(f"Internal server error: {error}")
        return jsonify(
            json_response(
                data={"error": "Internal Server Error"},
                status_code=500,
                message="An unexpected server error occurred",
                success=False
            )
        ), 500

    logger.info(f"{settings.APP_NAME} initialized successfully in {settings.APP_ENV} mode")
    return app


if __name__ == "__main__":
    settings = get_settings()
    app = create_app()
    app.run(host=settings.HOST, port=settings.PORT, debug=settings.DEBUG)
