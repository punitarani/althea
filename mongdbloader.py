import pymongo

# MongoDB configuration
MONGO_HOST = "bh3pyl4.mongodb.net"
MONGO_DB = "althea"
MONGO_USER = "weitao"
MONGO_PASSWORD = "rpGlMChHAaEr89WI"

# Connect to MongoDB
client = pymongo.MongoClient(f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}/{MONGO_DB}?retryWrites=true&w=majority")

# Access database and collection
db = client[MONGO_DB]
collection = db['openalex']  # Replace 'your_collection_name' with the actual collection name

# Query data
data = collection.find({})
for document in data:
    print(document)
