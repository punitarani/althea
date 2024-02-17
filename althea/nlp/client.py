"""althea/nlp/client.py"""

from openai import AsyncOpenAI, OpenAI

from althea import SECRETS

openai = AsyncOpenAI(api_key=SECRETS.OPENAI_API_KEY)

together = OpenAI(
    api_key=SECRETS.TOGETHER_API_KEY,
    base_url="https://api.together.xyz",
)
