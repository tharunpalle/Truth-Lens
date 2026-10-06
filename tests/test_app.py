"""
Integration and route tests for Flask application.
"""

import unittest
from src.app import create_app


class TestApp(unittest.TestCase):
    """Test core application endpoints."""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_health_check_endpoint(self):
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data["success"])
        self.assertEqual(data["data"]["status"], "operational")

    def test_status_endpoint(self):
        response = self.client.get("/status")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data["success"])
        self.assertIn("modules", data["data"])

    def test_home_page_serves_html(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Truth Lens", response.data)


if __name__ == "__main__":
    unittest.main()
