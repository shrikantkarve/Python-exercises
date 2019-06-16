#!/usr/bin/env python3

from pymongo import MongoClient
client = MongoClient()

db = client.pymongo_test

posts = db.posts

print(type(posts))

post_data = {
        "author": "Shrikant",
        "Title": "Sample mongodb project"
        }
result = posts.insert_one(post_data)
print("One post: {}".format(result.inserted_id))

bills_post = posts.find({"author": "Shrikant"})
for a in bills_post:
    print(a)




