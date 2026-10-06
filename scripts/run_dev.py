"""
Development Server Runner.
Launches Truth Lens in local development mode.
"""

import sys
from pathlib import Path

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.app import create_app
from src.config.settings import get_settings


def main():
    settings = get_settings()
    print("=" * 60)
    print(f"  {settings.APP_NAME} - Development Server")
    print(f"  Environment : {settings.APP_ENV}")
    print(f"  Local URL   : http://{settings.HOST}:{settings.PORT}")
    print(f"  Health Check: http://{settings.HOST}:{settings.PORT}/api/health")
    print("=" * 60)

    app = create_app()
    app.run(
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG
    )


if __name__ == "__main__":
    main()
