import google.generativeai as genai

from src.utils import load_env_variable


class GeminiAPIClient:
    def __init__(self):
        try:
            self.api_key = load_env_variable("GEMINI_API_KEY")
            self.model_name = load_env_variable("GEMINI_ID")
        except ValueError as e:
            print(f"Error loading API key: {e}")
            exit()
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name=self.model_name)

    def generate_response(self, prompt):
        """Generates a response from the Gemini API based on the prompt."""
        try:
            response = self.model.generate_content(prompt)
            if hasattr(response, "text"):
                return response.text
            else:
                return "Error: Unable to extract text from the response."
        except Exception as e:
            return f"Error: {e}"