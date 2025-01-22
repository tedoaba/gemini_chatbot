from api_client import GeminiAPIClient


class Chatbot:
    def __init__(self):
        self.api_client = GeminiAPIClient()
        self.chat_history = []

    def process_message(self, message):
        """Processes a user message, updates the chat history, and generates a response."""
        self.chat_history.append({"role": "user", "parts": [message]})
        prompt = self._prepare_prompt()
        response = self.api_client.generate_response(prompt)
        self.chat_history.append({"role": "model", "parts": [response]})
        return response

    def _prepare_prompt(self):
        """Prepares the prompt for the Gemini API, including the chat history."""
        return self.chat_history

    def clear_history(self):
      self.chat_history = []