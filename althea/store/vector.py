"""althea/store/vector.py"""

from pinecone import Pinecone

from althea import SECRETS

pc = Pinecone(api_key=SECRETS.PINECONE_API_KEY)
