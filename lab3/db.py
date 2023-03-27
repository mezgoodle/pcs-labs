# connect to the mongodb in the docker container

import datetime
import os

import pymongo


def get_db():
    # get the mongodb connection string
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb://localhost:27017")
    # connect to the mongodb
    client = pymongo.MongoClient(MONGODB_URI)
    # get the database
    db = client.example
    return db


# do some testing
if __name__ == "__main__":
    db = get_db()
    post = {
        "author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow(),
    }
    posts = db.posts
    post_id = posts.insert_one(post).inserted_id
    print(post_id)
