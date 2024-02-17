"""althea/nlp/embed.py"""

from client import openai

from .models import Document


async def chunk_text_into_documents(
    text: str, work_id: str, title: str
) -> list[Document]:
    """
    Chunk text into documents

    Args:
        text (str): Text to chunk
        work_id (str): Work ID
        title (str): Title of the work

    Returns:
        list[Document]: List of documents with the text and embeddings
    """

    documents = []

    # TODO: Chunk the text into documents

    # TODO: Embed the documents

    return documents


async def embed_text(text: str) -> list[float]:
    """Embed text using OpenAI's text-embedding-3-small model."""
    return (
        await openai.embeddings.create(input=[text], model="text-embedding-3-small")
        .data[0]
        .embedding
    )
