"""
Base Service Definition.

Defines the contract and common lifecycle for external services, API clients,
and data access handlers.
"""

from typing import Any, Dict, Optional
from src.utils.logger import get_logger


class BaseService:
    """
    Foundation service class to encapsulate external integrations and data pipelines.
    Subclasses will implement specific connector or business operations in subsequent phases.
    """

    def __init__(self, service_name: Optional[str] = None):
        self.service_name = service_name or self.__class__.__name__
        self.logger = get_logger(self.service_name)
        self.is_initialized = False

    def initialize(self) -> bool:
        """Lifecycle hook to establish connections or prepare resources."""
        self.logger.info(f"Initializing service: {self.service_name}")
        self.is_initialized = True
        return True

    def health_check(self) -> Dict[str, Any]:
        """Verify service operational status."""
        return {
            "service": self.service_name,
            "status": "healthy" if self.is_initialized else "uninitialized"
        }
