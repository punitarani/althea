"""althea/nlp/hallu.py"""

from .client import openai

HALLUCINATE_SYSTEM_PROMPT = """
You are a scientist working on a research project.
You are trying to come up with ideas for a new experiment.
You have a summary of the project and need to come up with ideas for the experiment.

You need very out-of-the-box ideas that are not constrained by the current state of technology.
You need to come up with ideas that are not limited by current scientific understanding.

List 5 ideas for experiments that could be conducted to test the hypothesis.
""".strip()


async def hallucinate_ideas(summary: str, direction: str) -> list[str]:
    """Hallucinate ideas based on a summary."""

    response = await openai.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": HALLUCINATE_SYSTEM_PROMPT},
            {"role": "user", "content": summary},
            {"role": "user", "content": direction},
        ],
        temperature=1,
    )
    return response.choices[0].message.content


BREAKDOWN_SYSTEM_PROMPT = """
You are a scientist working on a research project.
You are trying to break down a complex scientific research idea into simpler components.
You need to break down the idea into smaller, more manageable parts.
You need to understand the different aspects of the idea and how they relate to each other.
""".strip()


async def breakdown_idea(idea: str) -> list[str]:
    """Break down a complex scientific research idea into simpler components."""

    response = await openai.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": BREAKDOWN_SYSTEM_PROMPT},
            {"role": "user", "content": idea},
        ],
        temperature=0,
    )
    return response.choices[0].message.content
