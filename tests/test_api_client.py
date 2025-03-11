import unittest
from unittest.mock import patch, MagicMock
from src.api_client import GeminiAPIClient

class TestGeminiAPIClient(unittest.TestCase):

    @patch('src.utils.load_env_variable')
    @patch('google.generativeai.GenerativeModel')
    def test_generate_response(self, MockGenerativeModel, mock_load_env_variable):
        mock_load_env_variable.side_effect = ["fake_api_key", "fake_model_name"]
        mock_model_instance = MockGenerativeModel.return_value
        mock_model_instance.generate_content.return_value = MagicMock(text="Test response")
        
        client = GeminiAPIClient()
        prompt = [{"role": "user", "parts": ["Hello"]}]
        response = client.generate_response(prompt)
        
        self.assertEqual(response, "Test response")
        mock_model_instance.generate_content.assert_called_once_with(prompt)

if __name__ == '__main__':
    unittest.main()
