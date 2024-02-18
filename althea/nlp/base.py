"""althea/nlp/base.py"""

from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import Pinecone

from althea import SECRETS
from althea.store.vector import pc

embedding = OpenAIEmbeddings(
    api_key=SECRETS.OPENAI_API_KEY, model="text-embedding-3-small"
)

vectorstore = Pinecone(index=pc.Index("papers"), text_key="text", embedding=embedding)
