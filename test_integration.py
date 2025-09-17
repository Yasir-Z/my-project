import unittest
from app import app
import json

class FlaskIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_hello_and_echo_routes(self):
        # Test GET /
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello from Flask!")

        # Test POST /echo
        data = {"message": "Integration test"}
        response = self.client.post('/echo', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, data)

if __name__ == '__main__':
    unittest.main()

