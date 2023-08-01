import json
import boto3
from utils import get_secret
from pymongo import MongoClient


def get_db():
    client = MongoClient(get_secret())

    return client.academia

def handler(event, context):
    db = get_db()
    
    response = [item for item in db.users.find()]

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }