import boto3
import json
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "academia/mongodb"
    region_name = "us-east-1"

    #create a secret manager client
    session = boto3.session.Session()
    client = session.client(
        service_name = 'secretsmanager',
        region_name = region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId = secret_name
        )
    except ClientError as e:
        raise e
    
    secret = json.loads(get_secret_value_response['SecretString'])

    return secret["MONGODB_URI"]



