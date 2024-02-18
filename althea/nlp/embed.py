"""althea/nlp/embed.py"""

import tiktoken
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings

from .client import openai
from .models import Document, DocumentMetadata

text_splitter = SemanticChunker(OpenAIEmbeddings())

tokenizer = tiktoken.get_encoding("cl100k_base")


def get_token_count(text: str) -> int:
    """Get the number of tokens in the text."""
    return len(tokenizer.encode(text))


def split_chunk(chunk: str, max_tokens: int) -> list[str]:
    """
    Splits a large chunk of text into smaller chunks, each not exceeding the max_tokens limit.

    Args:
        chunk (str): The text chunk to split.
        max_tokens (int): The maximum number of tokens allowed per chunk.

    Returns:
        list[str]: A list of smaller text chunks.
    """
    if get_token_count(chunk) <= max_tokens:
        return [chunk]

    words = chunk.split()
    small_chunks = []
    current_chunk = []
    current_count = 0

    for word in words:
        word_count = get_token_count(word + " ")  # Include space in count
        if current_count + word_count > max_tokens:
            small_chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_count = word_count
        else:
            current_chunk.append(word)
            current_count += word_count

    if current_chunk:  # Add the last chunk if any
        small_chunks.append(" ".join(current_chunk))

    return small_chunks


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

    # Make sure no chunk exceeds the token limit of 4096
    chunks = []
    for chunk in [doc.page_content for doc in docs]:
        chunks.extend(split_chunk(chunk, 4096))

    # Embed the documents
    embeddings = await batch_embed_text(chunks)

    for idx, (doc, embedding) in enumerate(zip(docs, embeddings)):
        # Create a document
        documents.append(
            Document(
                id=f"{work_id}-{idx}",
                values=embedding,
                metadata=DocumentMetadata(
                    work_id=work_id,
                    title=title,
                    index=idx,
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


async def batch_embed_text(texts: list[str]) -> list[list[float]]:
    """
    Embed a batch of texts using OpenAI's text-embedding-3-small model, ensuring each batch of texts
    does not exceed the token limit for the API call.

    Args:
        texts (list[str]): List of texts to embed.

    Returns:
        list[list[float]]: List of embeddings for each text.
    """
    token_counts = [get_token_count(text) for text in texts]
    token_limit = 4096
    embeddings = []

    # Initialize the first batch
    current_batch = []
    current_tokens = 0

    for text, count in zip(texts, token_counts):
        # Check if adding this text would exceed the token limit
        if current_tokens + count > token_limit:
            # Embed the current batch before exceeding the limit
            if current_batch:
                batch_embeddings = await openai.embeddings.create(
                    input=current_batch, model="text-embedding-3-small"
                )
                embeddings.extend(
                    [embedding.embedding for embedding in batch_embeddings.data]
                )
            # Start a new batch with the current text
            current_batch = [text]
            current_tokens = count
        else:
            # Add the current text to the batch
            current_batch.append(text)
            current_tokens += count

    # Don't forget to embed the last batch
    if current_batch:
        batch_embeddings = await openai.embeddings.create(
            input=current_batch, model="text-embedding-3-small"
        )
        embeddings.extend([embedding.embedding for embedding in batch_embeddings.data])

    return embeddings
