import json

from althea.nlp.base import vectorstore
from althea.nlp.client import openai
from althea.nlp.hallu import breakdown_idea, hallucinate_ideas
from althea.nlp.search import search_web, search_wiki

PLANNER_SYSTEM_PROMPT = """
You are a scientist working on a research project.
You should use research assistants to break down the objective into smaller, more manageable parts.
Then, you should assign each part to the most suitable assistant to perform the task to sequentially achieve the objective.

You are given 4 assistants to help you with an objective.
1. web - An internet search assistant to help you find relevant information.
2. wiki - A knowledge assistant to help you understand the information from wikipedia.
3. writer - A writing assistant to help you write about a topic using only the context, objective and memory.
4. memory - A memory assistant to help you fetch relevant information from scientific papers and literature only.

You need to plan the research project with the help of these assistants.
You need to simplify the objective into smaller, more manageable parts.
Then, you need to assign each part to the most suitable assistant.

You must return the plan in JSON format with a single root key "plan" and a list of tasks with keys "agent" and "task".

[EXAMPLE]
context: "I am trying to understand the effects of climate change on the biodiversity of the Amazon rainforest."
objective: "How does deforestation affect the biodiversity of the Amazon rainforest?"

assistant:
{
  "plan": [
    {
      "agent": "web",
      "task": "What is the current state of the Amazon rainforest?"
    },
    {
      "agent": "wiki",
      "task": "What is a carbon sink?"
    },
    {
      "agent": "memory",
      "task": "What are the effects of deforestation on the Amazon rainforest?"
    },
    {
      "agent": "writer",
      "task": "Write a summary of the effects of deforestation on the Amazon rainforest."
    }
  ]
}

[END EXAMPLE]
"""


async def research(summary: str, direction: str) -> list[list[str]]:
    """Research a scientific idea."""
    ideas = await hallucinate_ideas(summary, direction)
    breakdown = await breakdown_idea(ideas[0])

    responses = []

    ctx = summary
    for step in breakdown:
        print(step)

        plan = await research_planner(ctx, step)
        print(plan)

        response = await research_executor(plan)
        responses.append(response)
        print(response)

        ctx += "\n".join(response)

    return responses


async def research_planner(context: str, objective: str) -> list[str, str]:
    """Plan the research project."""

    response = await openai.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": PLANNER_SYSTEM_PROMPT},
            {"role": "user", "content": context},
            {"role": "user", "content": objective},
        ],
        response_format={"type": "json_object"},
        temperature=0.25,
    )

    return json.loads(response.choices[0].message.content).get("plan", [])


async def research_executor(plan: list[str, str]) -> list[str]:
    """Execute the research plan."""
    responses = []
    context = ""
    for task in plan:
        agent, task = task["agent"], task["task"]
        response = await run_agent(agent, task, context)
        responses.append(response)
        context += response + "\n"
        print(f"{agent}: {task}\n{response}\n\n\n")
    return responses


async def search_memory(question: str) -> str:
    """Search the memory for the answer to a question."""
    retriever = vectorstore.as_retriever(k=10, search_type="mmr")
    docs = retriever.get_relevant_documents(question)
    return "\n".join([doc.page_content for doc in docs])


async def write(task: str, context: str) -> str:
    """Write about a topic using only the context, objective and memory."""
    response = await openai.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
                "role": "system",
                "content": "You are a writer for a research scientist. You are given a task and context information to write about.",
            },
            {"role": "user", "content": context},
            {"role": "user", "content": task},
        ],
        temperature=0,
    )

    return response.choices[0].message.content


async def run_agent(agent: str, task: str, context: str) -> str:
    """Execute the task using the agent."""
    if agent == "web":
        return await search_web(task)
    elif agent == "wiki":
        return await search_wiki(task)
    elif agent == "memory":
        return await search_memory(task)
    elif agent == "writer":
        return await write(task, context)


if __name__ == "__main__":
    import asyncio

    _summary = """The paper provides an overview of empirical force fields for biomolecular simulations. Key points:
- Empirical force fields allow for computational studies of biomolecules at atomic detail. They are comprised of a potential energy function and parameters optimized to reproduce experimental data. 
- The most common form is a Class I additive potential with terms for bonds, angles, torsions, and nonbonded van der Waals and electrostatic interactions. Some newer force fields include explicit polarization.
- Force fields differ in their parameter optimization methodology. Some target quantum mechanical data on small molecules, others use knowledge-based approaches to reproduce experimental condensed phase properties directly.
- Several widely used biomolecular force fields are reviewed, including CHARMM, AMBER, OPLS, and GROMOS. Each has strengths and weaknesses depending on the type of system and properties of interest.
- Force fields for proteins, nucleic acids, lipids, and carbohydrates are discussed. Heterogeneous biomolecular systems and drug-like molecules present challenges due to the need to balance parameters appropriately.
- Continuous force field optimization is needed as new experimental data and technical capabilities become available. Progress has been made but further improvements in accuracy are possible.
- Overall, when properly developed and applied, empirical force fields enable valuable atomic-level insights into biomolecular structure and interactions. But results should be interpreted considering the specifics of the force field used."""
    _direction = "Empirical forces for treating tumors"

    result = asyncio.run(research(_summary, _direction))
    print(result)
