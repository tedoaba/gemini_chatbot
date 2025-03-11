"""Chatbot class for processing user messages and generating responses."""

from src.api_client import GeminiAPIClient


class Chatbot:
    """Chatbot for processing user messages and generating responses."""

    def __init__(self):
        """Initialize the Chatbot with an API client and chat history."""
        self.api_client = GeminiAPIClient()
        self.chat_history = []

    def process_message(self, message):
        """Process a user message, update history, and generate a response."""
        self.chat_history.append({"role": "user", "parts": [message]})
        prompt = self._prepare_prompt()
        response = self.api_client.generate_response(prompt)
        self.chat_history.append({"role": "model", "parts": [response]})
        return response

    def _prepare_prompt(self):
        """Prepare the prompt for the Gemini API, with the chat history."""
        return self.chat_history

    def clear_history(self):
        """Clear the chat history."""
        self.chat_history = []
