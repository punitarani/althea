"""althea/nlp/search.py"""

from .client import cohere


async def search_web(question: str) -> str:
    """Search the internet for the answer to a question."""

    prediction = await cohere.chat(
        message=question,
        preamble_override="You are a scientific research assistant. You answer questions concisely and accurately.",
        model="command",
        temperature=0.25,
        stream=False,
        citation_quality="accurate",
        connectors=[{"id": "web-search"}],
        documents=[],
    )
    return prediction.text


async def search_wiki(question: str) -> str:
    """Search Wikipedia for the answer to a question."""

    prediction = await cohere.chat(
        message=question,
        preamble_override="You are a scientific research assistant. You answer questions concisely and accurately.",
        model="command-light",
        temperature=0.25,
        stream=False,
        citation_quality="accurate",
        connectors=[
            {"id": "web-search", "options": {"site": "https://www.wikipedia.org/"}}
        ],
        documents=[],
    )
    return prediction.text
