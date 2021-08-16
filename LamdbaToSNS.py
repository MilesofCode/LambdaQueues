import boto3
import json
from botocore.exceptions import ClientError
from botocore.config import Config
from botocore.vendored import requests


def lambda_handler(event, context):
    # Generates presigned url
    client = boto3.client("s3", region_name='REGION',
                          aws_access_key_id='ACCESS_KEY',
                          aws_secret_access_key='SECRET_ACCESS_KEY')
    try:
        response = client.generate_presigned_url('get_object',
                                                 Params={'Bucket': 'BUCKET_NAME', 'Key': 'OBJECT_NAME'},
                                                 ExpiresIn=3600)
        print(response)
    except ClientError as e:
        print(e)

    ses_client = boto3.client("ses", region_name="us-west-2")
    CHARSET = "UTF-8"

# Sends email to target email
    email = ses_client.send_email(
        Destination={
            "ToAddresses": [
                "TARGET_EMAIL",
            ],
        },
        Message={
            "Body": {
                "Text": {
                    "Charset": CHARSET,
                    "Data": "MESSAGE_HERE",
                }
            },
            "Subject": {
                "Charset": CHARSET,
                "Data": "SUBJECT_LINE_HERE",
            },
        },
        Source="SOURCE_EMAIL",
    )
    return response, email
