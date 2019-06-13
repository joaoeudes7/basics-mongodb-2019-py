from pprint import pprint
from datetime import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

blog_database = client.blog
users_collection = blog_database.users
articles_collection = blog_database.articles

author = 'joaoeudes7'

article = {
    "title": "My first post",
    "body": "The body of the amazing post would go here.",
    "author": author,
    "tags": ["ken", "general", "admin", "Oregon"],
    "posted": datetime.now()
}

# Let's check to make sure the author exists before inserting
if users_collection.find_one({"username": author}):
    users_collection.find_one({ 'username': author })
    document = articles_collection.insert_one(article)
    pprint(article)
else:
    print(f"Author {author} is not a current user")

