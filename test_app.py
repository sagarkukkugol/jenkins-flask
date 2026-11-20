import unittest
from app import app

class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data.decode(), "Hello from Flask Jenkins!")

if __name__ == '__main__':
    unittest.main()
