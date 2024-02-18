"""althea/nlp/client.py"""

import cohere
from openai import AsyncOpenAI, OpenAI

from althea import SECRETS

cohere = cohere.AsyncClient(api_key=SECRETS.COHERE_API_KEY)

openai = AsyncOpenAI(api_key=SECRETS.OPENAI_API_KEY)

together = OpenAI(
    api_key=SECRETS.TOGETHER_API_KEY,
    base_url="https://api.together.xyz",
)
