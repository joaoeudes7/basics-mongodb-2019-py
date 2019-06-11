from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/local")

blogDatabase = client.blog
usersCollection = blogDatabase.users

ken = {
    "username": "kalger",
    "password": "password",
    "lang": "EN"
}

usersCollection.insert_one(ken)

user = usersCollection.find_one()

print(user)

