"""Utility functions for the Gemini Chatbot."""

import os
from dotenv import load_dotenv


def load_env_variable(key):
    """Load an environment variable, handling them and system variables."""
    load_dotenv()
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"Environment variable {key} is not set.")
    return value
