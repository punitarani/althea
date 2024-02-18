"""althea/nlp/hallu.py"""

import json

from .client import openai

HALLUCINATE_SYSTEM_PROMPT = """
You are a scientist working on a research project.
You are trying to come up with ideas for a new experiment.
You have a summary of the project and need to come up with ideas for the experiment.

You need very out-of-the-box ideas that are not constrained by the current state of technology.
You need to come up with ideas that are not limited by current scientific understanding.

Each idea should be very clear and should not require any further explanation or context.

List 5 ideas for experiments that could be conducted to test the hypothesis.
List the ideas in JSON format with a single root key "ideas" and a list of strings as the value.
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
        response_format={"type": "json_object"},
        temperature=1,
    )
    return json.loads(response.choices[0].message.content).get("ideas", [])


BREAKDOWN_SYSTEM_PROMPT = """
You are a scientist working on a research project.
You are trying to break down a complex scientific research idea into simpler components.
You need to break down the idea into smaller, more manageable parts.
You need to understand the different aspects of the idea and how they relate to each other.

All the steps should be exploratory research through previous experiments and literature review.
Do not include any steps that requires conducting new experiments or collecting new data.
It should be a logical progression of steps that build on each other and lead to a conclusion.

Each step should be very clear and should not require any further explanation or context.
The step should be very specific and should not be too broad or general.

List the different steps in logical order in JSON format.
It should have a single root key "steps" and a list of strings as the value.
""".strip()


async def breakdown_idea(idea: str) -> list[str]:
    """Break down a complex scientific research idea into simpler components."""

    response = await openai.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": BREAKDOWN_SYSTEM_PROMPT},
            {"role": "user", "content": idea},
        ],
        response_format={"type": "json_object"},
        temperature=0,
    )
    return json.loads(response.choices[0].message.content).get("steps", [])
