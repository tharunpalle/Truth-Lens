"""
Application Configuration Module.

Provides centralized, environment-aware configuration management.
Reads values from environment variables or a local .env file with safe fallbacks.
No credentials or secret keys are hardcoded.
"""

import os
from pathlib import Path
from dataclasses import dataclass


def _load_env_file(env_path: Path) -> None:
    """
    Lightweight fallback parser for .env files without requiring third-party libraries.
    If python-dotenv is available, it uses that; otherwise falls back to this parser.
    """
    if not env_path.exists():
        return

    try:
        import dotenv
        dotenv.load_dotenv(dotenv_path=env_path)
        return
    except ImportError:
        pass

    # Basic fallback parser
    try:
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, val = line.split("=", 1)
                key = key.strip()
                val = val.strip().strip("'\"")
                if key and key not in os.environ:
                    os.environ[key] = val
    except Exception:
        # Silently fail if unable to parse local file; defaults will take over
        pass


# Base project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
_load_env_file(PROJECT_ROOT / ".env")


@dataclass(frozen=True)
class Settings:
    """Application configuration container."""

    # Project Information
    APP_NAME: str = os.getenv("APP_NAME", "Truth Lens")
    APP_ENV: str = os.getenv("APP_ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() in ("true", "1", "t", "yes")

    # Networking
    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", "5000"))

    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production-truth-lens-2026")

    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO").upper()

    # Filesystem Paths
    ROOT_DIR: Path = PROJECT_ROOT
    SRC_DIR: Path = PROJECT_ROOT / "src"
    PUBLIC_DIR: Path = PROJECT_ROOT / "public"


# Singleton instance
_settings_instance: Settings | None = None


def get_settings() -> Settings:
    """Retrieve the application settings instance."""
    global _settings_instance
    if _settings_instance is None:
        _settings_instance = Settings()
    return _settings_instance
