"""althea/nlp/embed.py"""

from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings

from .client import openai
from .models import Document, DocumentMetadata

text_splitter = SemanticChunker(OpenAIEmbeddings())


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

    # Semantically chunk the text into documents
    docs = text_splitter.create_documents([text])

    # Embed the documents
    embeddings = await openai.embeddings.create(
        input=[doc.page_content for doc in docs], model="text-embedding-3-small"
    )

    for idx, (doc, embedding) in enumerate(zip(docs, embeddings.data)):
        # Create a document
        documents.append(
            Document(
                id=work_id,
                values=embedding.embedding,
                metadata=DocumentMetadata(
                    index=idx,
                    title=title,
                    text=doc.page_content,
                ),
            )
        )

    return documents


async def embed_text(text: str) -> list[float]:
    """Embed text using OpenAI's text-embedding-3-small model."""
    return (
        await openai.embeddings.create(input=[text], model="text-embedding-3-small")
        .data[0]
        .embedding
    )
