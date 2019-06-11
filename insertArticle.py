import datetime
import pprint

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/local")

blogDatabase = client.blog
usersCollection = blogDatabase.users
articlesCollection = blogDatabase.articles

author = 'kalger'

article = {
    "title": "My first post",
    "body": "The body of the amazing post would go here.",
    "author": author,
    "tags": ["ken", "general", "admin", "Oregon"],
    "posted": datetime.datetime.now()
}

# Let's check to make sure the author exists before inserting

if usersCollection.find_one({"username": author}):
    document = articlesCollection.insert_one(article)
    pprint.pprint(article)
else:
    raise ValueError("Author {} is not a current user".format(author))

