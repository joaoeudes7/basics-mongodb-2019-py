from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

blog_database = client.blog
users_collection = blog_database.users
articles_collection = blog_database.articles

randomUser = users_collection.find_one()

print(randomUser)

karmaCount = users_collection.find({"karma": {"$gte": 450, "$lte": 475}}).count()

print(karmaCount)

# Add Comments to an article
articles_collection.update({"_id": 19}, {"$set": {"comments": []}})

# Update Comments
articles_collection.update({"_id": 19}, {
    "$push":
    {
        "comments":
        {
            "username": "mary",
            "comment": "Great first post."
        }
    }
})

# Delete Article
articles_collection.remove({"_id": 25})
