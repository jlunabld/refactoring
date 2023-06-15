import unittest
from app import RMSDashboard

class TestRMSDashboard(unittest.TestCase):
    def setUp(self):
        self.app = RMSDashboard().app
        self.client = self.app.test_client()

    def test_layout(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<div>', response.data)

if __name__ == '__main__':
    unittest.main()