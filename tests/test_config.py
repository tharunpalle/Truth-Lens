"""
Unit tests for configuration module.
"""

import unittest
from src.config.settings import Settings, get_settings


class TestSettings(unittest.TestCase):
    """Test application settings resolution and defaults."""

    def test_default_settings(self):
        settings = get_settings()
        self.assertIsNotNone(settings.APP_NAME)
        self.assertIsInstance(settings.PORT, int)
        self.assertIsInstance(settings.DEBUG, bool)
        self.assertTrue(settings.ROOT_DIR.exists())
        self.assertTrue(settings.SRC_DIR.exists())

    def test_settings_singleton(self):
        s1 = get_settings()
        s2 = get_settings()
        self.assertIs(s1, s2)


if __name__ == "__main__":
    unittest.main()
