import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Creates a test client
        self.app = app.test_client()
        self.app.testing = True  # Propagate exceptions to the test client

    def test_hello_route(self):
        # Send GET request to "/"
        response = self.app.get('/')
        
        # Check status code
        self.assertEqual(response.status_code, 200)
        
        # Check response data (bytes)
        self.assertEqual(response.data, b"Hello from Flask!")

if __name__ == '__main__':
    unittest.main()

