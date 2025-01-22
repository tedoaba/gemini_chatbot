import os
from dotenv import load_dotenv


def load_env_variable(key):
    """Loads an environment variable, handling .env file and system variables."""
    load_dotenv()
    value = os.getenv(key)
    if value is None:
        raise ValueError(f"Environment variable {key} is not set.")
    return value