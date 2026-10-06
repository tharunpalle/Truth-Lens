"""
Base Model Definition.

Provides a common foundation for domain data models and schemas.
Ensures standardized serialization, identification, and timestamps.
"""

from dataclasses import dataclass, field, asdict
from typing import Dict, Any, Optional
import uuid
from src.utils.helpers import get_utc_timestamp


@dataclass
class BaseModel:
    """
    Abstract foundation model offering ID generation, timestamps,
    and dictionary serialization.
    """
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: str = field(default_factory=get_utc_timestamp)
    updated_at: str = field(default_factory=get_utc_timestamp)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize model instance to a dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BaseModel":
        """Instantiate a model instance from dictionary data."""
        return cls(**{k: v for k, v in data.items() if k in cls.__dataclass_fields__})
