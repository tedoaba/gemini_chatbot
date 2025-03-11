"""Unit tests for the Chatbot class."""

import unittest
from unittest.mock import patch
from src.chatbot import Chatbot


class TestChatbot(unittest.TestCase):
    """Test cases for the Chatbot class."""

    @patch("src.api_client.GeminiAPIClient.generate_response")
    def test_process_message(self, mock_generate_response):
        """Test the process_message method."""
        mock_generate_response.return_value = "Test response"
        chatbot = Chatbot()

        user_message = "Hello"
        response = chatbot.process_message(user_message)

        self.assertEqual(response, "Test response")
        self.assertEqual(len(chatbot.chat_history), 2)
        self.assertEqual(chatbot.chat_history[0]["role"], "user")
        self.assertEqual(chatbot.chat_history[0]["parts"], [user_message])
        self.assertEqual(chatbot.chat_history[1]["role"], "model")
        self.assertEqual(chatbot.chat_history[1]["parts"], [response])

    def test_clear_history(self):
        """Test the clear_history method."""
        chatbot = Chatbot()
        chatbot.chat_history = [{"role": "user", "parts": ["Hello"]}]

        chatbot.clear_history()

        self.assertEqual(chatbot.chat_history, [])


if __name__ == "__main__":
    unittest.main()
