from pprint import pprint
from pymongo import MongoClient

# mongodb://${MONGO_USER}:${MONGO_PASSWORD}
client = MongoClient("mongodb://localhost:27017")

blog_database = client.get_database('blog')
users_collection = blog_database.get_collection('users')

def creatUserBlog(username, password):
    user = {
        "username": username,
        "password": password
    }

    users_collection.insert_one(user)

    for doc in users_collection.find({}):
        pprint(doc)


creatUserBlog("antonio", "hahah")

users_collection.delete_many({ "username": "antonio" })

