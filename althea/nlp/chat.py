"""althea/nlp/chat.py"""

from langchain_community.vectorstores import Pinecone
from langchain_openai import OpenAIEmbeddings

from althea import SECRETS
from althea.store.vector import pc

embedding = OpenAIEmbeddings(
    api_key=SECRETS.OPENAI_API_KEY, model="text-embedding-3-small"
)
vectorstore = Pinecone(index=pc.Index("papers"), text_key="text", embedding=embedding)
retriever = vectorstore.as_retriever(k=5)

# TODO: build a chatbot

if __name__ == "__main__":
    query = "What is an amino acid?"
    docs = vectorstore.similarity_search(query)
    print(docs)
