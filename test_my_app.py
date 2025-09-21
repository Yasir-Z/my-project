"""Unit tests for Flask app endpoints."""

import unittest
from app import app  # First-party import


class FlaskAppTest(unittest.TestCase):
    """Test cases for Flask app routes."""

    def setUp(self):
        """Set up test client."""
        self.client = app.test_client()
        self.client.testing = True

    def test_homepage(self):
        """Test the '/' route returns status 200 and contains 'Hello'."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello", response.data)


if __name__ == "__main__":
    unittest.main()
