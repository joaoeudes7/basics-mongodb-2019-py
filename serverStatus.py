from pprint import pprint
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

uri = "mongodb://localhost:27017"
client = MongoClient(uri)

try:
    status = client.admin.command("serverStatus")
    print("Connected to MongoDB Atlas with status: ")
    pprint.pprint(status)

except ConnectionFailure:
    print("MongoDB Atlas connection not established.")

