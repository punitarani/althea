"""althea/store/mongo.py"""

from pymongo.mongo_client import MongoClient

from althea import SECRETS

MONGO_URI = f"mongodb+srv://{SECRETS.MONGO_USERNAME}:{SECRETS.MONGO_PASSWORD}@{SECRETS.MONGO_DB}.{SECRETS.MONGO_HOST}/?retryWrites=true&w=majority"
mongo_client = MongoClient(MONGO_URI)
