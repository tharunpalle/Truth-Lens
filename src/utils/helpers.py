"""
General Helper Utilities.

Contains reusable helper functions for formatting, sanitization, and response shaping.
"""

from datetime import datetime, timezone
from typing import Any, Dict, Tuple


def get_utc_timestamp() -> str:
    """Returns current UTC timestamp in ISO-8601 format."""
    return datetime.now(timezone.utc).isoformat()


def json_response(
    data: Any = None,
    status_code: int = 200,
    message: str = "Success",
    success: bool = True
) -> Dict[str, Any]:
    """
    Constructs a uniform JSON API response dictionary.
    """
    response_payload: Dict[str, Any] = {
        "success": success,
        "status": status_code,
        "message": message,
        "timestamp": get_utc_timestamp(),
        "data": data if data is not None else {}
    }
    return response_payload


def sanitize_text(value: str) -> str:
    """Strip whitespace and dangerous null bytes from string input."""
    if not isinstance(value, str):
        return ""
    return value.replace("\x00", "").strip()
