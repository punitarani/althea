"""althea/nlp/chat.py"""

from .base import vectorstore

retriever = vectorstore.as_retriever(k=5)

# TODO: build a chatbot

if __name__ == "__main__":
    query = "What is an amino acid?"
    docs = vectorstore.similarity_search(query)
    print(docs)
