"""althea/secrets.py"""

import os

from pydantic import BaseModel


class Secrets(BaseModel):
    """Secrets loaded from environment variables"""

    # OpenAI
    OPENAI_API_KEY: str

    # Mongo
    MONGO_HOST: str
    MONGO_DB: str
    MONGO_USERNAME: str
    MONGO_PASSWORD: str

    @classmethod
    def load(cls) -> "Secrets":
        """Load secrets from environment variables"""
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        assert OPENAI_API_KEY, "OPENAI_API_KEY environment variable not set"

        # Mongo
        MONGO_HOST = os.getenv("MONGO_HOST")
        MONGO_DB = os.getenv("MONGO_DB")
        MONGO_USERNAME = os.getenv("MONGO_USER")
        MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
        assert MONGO_HOST, "MONGO_HOST environment variable not set"
        assert MONGO_DB, "MONGO_DB environment variable not set"
        assert MONGO_USERNAME, "MONGO_USERNAME environment variable not set"
        assert MONGO_PASSWORD, "MONGO_PASSWORD environment variable not set"

        return cls(
            OPENAI_API_KEY=OPENAI_API_KEY,
            MONGO_HOST=MONGO_HOST,
            MONGO_DB=MONGO_DB,
            MONGO_USERNAME=MONGO_USERNAME,
            MONGO_PASSWORD=MONGO_PASSWORD,
        )