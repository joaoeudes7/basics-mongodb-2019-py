from pymongo import MongoClient

root = MongoClient("mongodb://localhost:27017")

blog_database = root.blog
users_collection = blog_database.users

user = {
    "username": "joaoeudes7",
    "password": "hi123456",
}

users_collection.insert_one(user)

user = users_collection.find_one()

print(user)

