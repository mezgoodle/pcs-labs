# connect to the mongodb in the docker container

import datetime
import os

import pymongo


def get_db():
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb://localhost:27017")
    client = pymongo.MongoClient(MONGODB_URI, username="root", password="root")
    db = client.cafes
    return db


# do some testing
if __name__ == "__main__":
    db = get_db()
    cafes = db.cafes
    new_cafes = [
        {
            "name": "Starbucks",
            "location": "New York",
            "rating": 4.5,
        },
        {
            "name": "Cafe Coffee Day",
            "location": "Bangalore",
            "rating": 4.0,
        },
        {
            "name": "Dunkin Donuts",
            "location": "New York",
            "rating": 4.0,
        },
        {
            "name": "Tim Hortons",
            "location": "Toronto",
            "rating": 4.0,
        },
    ]
    result = cafes.insert_many(new_cafes)
    result.inserted_ids
