import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.data.decode(), 'Hello World')
        
    def test_hello(self):
        response = self.app.post('/hello', data={'name': 'John'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Hello John', response.data.decode())
        
if __name