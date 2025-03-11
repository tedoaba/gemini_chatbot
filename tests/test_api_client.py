"""Unit tests for the GeminiAPIClient class."""

import unittest
from unittest.mock import patch, MagicMock
from src.api_client import GeminiAPIClient


class TestGeminiAPIClient(unittest.TestCase):
    """Test cases for the GeminiAPIClient class."""

    @patch("src.utils.load_env_variable")
    @patch("google.generativeai.GenerativeModel")
    def test_generate_response(self, MockGenerativeModel, mock_env_variable):
        """Test the generate_response method."""
        mock_env_variable.side_effect = ["fake_api_key", "fake_model_name"]
        mock_model_instance = MockGenerativeModel.return_value
        mock_model_instance.generate_content.return_value = MagicMock(
            text="Test response"
        )

        client = GeminiAPIClient()
        prompt = [{"role": "user", "parts": ["Hello"]}]
        response = client.generate_response(prompt)

        self.assertEqual(response, "Test response")
        mock_model_instance.generate_content.assert_called_once_with(prompt)


if __name__ == "__main__":
    unittest.main()
