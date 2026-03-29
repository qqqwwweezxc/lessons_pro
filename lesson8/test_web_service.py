import unittest
from unittest.mock import patch, Mock
from web_service import WebService
import requests

class TestWebService(unittest.TestCase):

    def setUp(self):
        self.service = WebService()

    @patch("web_service.requests.get")
    def test_get_data_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = self.service.get_data("https://example.com")
        self.assertEqual(result, {"data": "test"})
        mock_get.assert_called_once_with("https://example.com")

    @patch("web_service.requests.get")
    def test_get_data_404(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
        mock_get.return_value = mock_response

        result = self.service.get_data("https://example.com/notfound")
        self.assertEqual(result, {})

    @patch("web_service.requests.get")
    def test_get_data_request_exception(self, mock_get):
        mock_get.side_effect = requests.RequestException("Network error")

        result = self.service.get_data("https://example.com/error")
        self.assertEqual(result, {})

if __name__ == "__main__":
    unittest.main()
    