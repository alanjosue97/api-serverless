import json

from bson import ObjectId

from utils import get_secret
from pymongo import MongoClient

def get_db():
    client = MongoClient(get_secret())

    return client.academia

def handler(event, context):
    db = get_db()
    
    db.users.insert_one(
        {
            "_id": str(ObjectId()),
            "name": "Alan",
        }
    )

    

    return {
        "statusCode": 200,
        "body": json.dumps({"messange": "User created"})
    }