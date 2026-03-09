import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self, openai_key, model_id="gpt-4o-mini"):
        self.openai_key = openai_key
        self.model_id = model_id


def get_settings():
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError(
            "Missing OPENAI_API_KEY. Put it in a .env file or export it in your shell."
        )

    model_id = os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip()
    return Settings(openai_key=api_key, model_id=model_id)