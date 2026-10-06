"""
Logging Utility.

Provides standard structured logging for the application.
"""

import logging
import sys
from src.config.settings import get_settings


def setup_logger(name: str = "truth_lens") -> logging.Logger:
    """
    Configures and returns a logger instance with consistent formatting.
    """
    settings = get_settings()
    log_level = getattr(logging, settings.LOG_LEVEL, logging.INFO)

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Avoid duplicate handlers if already configured
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(log_level)
        formatter = logging.Formatter(
            fmt="[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def get_logger(name: str = "truth_lens") -> logging.Logger:
    """Convenience getter for loggers."""
    return setup_logger(name)
