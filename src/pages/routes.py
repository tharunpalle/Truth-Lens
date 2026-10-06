"""
Application Page Routes and Views.

Defines blueprint routes for serving web pages and UI endpoints.
"""

from pathlib import Path
from flask import Blueprint, send_from_directory, jsonify
from src.config.settings import get_settings
from src.utils.helpers import json_response

pages_bp = Blueprint("pages", __name__)
settings = get_settings()


@pages_bp.route("/")
def home():
    """Serves the primary web application landing page."""
    public_dir = settings.PUBLIC_DIR
    index_file = public_dir / "index.html"
    if index_file.exists():
        return send_from_directory(public_dir, "index.html")
    return jsonify(json_response(data={"message": "Truth Lens Foundation Active"}))


@pages_bp.route("/status")
def status_page():
    """Returns foundation modules operational status."""
    status_info = {
        "application": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "modules": {
            "components": "Ready",
            "pages": "Ready",
            "services": "Ready",
            "utils": "Ready",
            "models": "Ready",
            "config": "Ready",
            "public": "Ready",
            "tests": "Ready"
        }
    }
    return jsonify(json_response(data=status_info))
