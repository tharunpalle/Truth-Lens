"""
Unit tests for utility helpers.
"""

import unittest
from src.utils.helpers import json_response, get_utc_timestamp, sanitize_text


class TestUtils(unittest.TestCase):
    """Test utility helper functions."""

    def test_get_utc_timestamp(self):
        ts = get_utc_timestamp()
        self.assertIsInstance(ts, str)
        self.assertTrue(len(ts) > 10)

    def test_json_response_structure(self):
        resp = json_response(data={"item": 123}, status_code=200, message="OK")
        self.assertTrue(resp["success"])
        self.assertEqual(resp["status"], 200)
        self.assertEqual(resp["message"], "OK")
        self.assertEqual(resp["data"]["item"], 123)
        self.assertIn("timestamp", resp)

    def test_sanitize_text(self):
        raw = "  hello world\x00  "
        clean = sanitize_text(raw)
        self.assertEqual(clean, "hello world")


if __name__ == "__main__":
    unittest.main()
