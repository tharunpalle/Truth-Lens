"""
Base Component Definition.

Provides a common interface for reusable application components,
renderable blocks, or modular UI pieces.
"""

from typing import Dict, Any


class BaseComponent:
    """
    Abstract representation of a reusable visual or functional component.
    """

    def __init__(self, name: str, props: Dict[str, Any] | None = None):
        self.name = name
        self.props = props or {}

    def render(self) -> str:
        """Render the component representation."""
        return f"<!-- Component: {self.name} -->"
