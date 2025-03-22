import unittest
from unittest.mock import patch
import httputil

class TestHttpUtil(unittest.TestCase):

    @patch('httputil.requests.get')
    def test_get_success(self, mock_get):
        # 模拟成功的响应
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'key': 'value'}

        response = httputil.get('https://api.example.com/data', params={'key': 'value'})
        self.assertEqual(response, {'key': 'value'})
        mock_get.assert_called_once_with('https://api.example.com/data', params={'key': 'value'}, headers=None)

    @patch('httputil.requests.get')
    def test_get_failure(self, mock_get):
        # 模拟失败的响应
        mock_get.return_value.status_code = 404

        with self.assertRaises(Exception):
            httputil.get('https://api.example.com/data')

    @patch('httputil.requests.post')
    def test_post_success(self, mock_post):
        # 模拟成功的响应
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {'key': 'value'}

        response = httputil.post('https://api.example.com/data', data={'key': 'value'})
        self.assertEqual(response, {'key': 'value'})
        mock_post.assert_called_once_with('https://api.example.com/data', json={'key': 'value'}, headers=None)

    @patch('httputil.requests.post')
    def test_post_failure(self, mock_post):
        # 模拟失败的响应
        mock_post.return_value.status_code = 400

        with self.assertRaises(Exception):
            httputil.post('https://api.example.com/data', data={'key': 'value'})

if __name__ == '__main__':
    unittest.main() 