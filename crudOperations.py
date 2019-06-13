from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

blog_database = client.get_database('blog')
users_collection = blog_database.get_collection('users')
articles_collection = blog_database.get_collection('articles')

user = users_collection.find_one()

print(user)

countDocs = users_collection.count_documents({ "username": "joaoeudes7"})

print(countDocs)

something_article = articles_collection.find_one()

# Add Comments to an article
articles_collection.update_one({ "_id": something_article['_id'] }, {"$set": {"comments": []}})

# Update Comments
articles_collection.update_one({ "_id": something_article['_id'] }, {
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
# articles_collection.delete_one({"_id": 25})
