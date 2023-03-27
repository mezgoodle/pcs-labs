# connect to the mongodb in the docker container

import os

import pymongo


def get_db():
    # get the mongodb connection string
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb://localhost:27017")
    # connect to the mongodb
    client = pymongo.MongoClient(MONGODB_URI)
    # get the database
    db = client.get_default_database()
    return db


# do some testing
if __name__ == "__main__":
    db = get_db()
    print(db)
    print(db.list_collection_names())
