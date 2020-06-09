import unittest
from app import app


class TestAdd(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_page(self):
        response = self.app.get('/data', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
