import json
import boto3

def lambda_handler(event, context):
    username = event['username']
    sns = boto3.client('sns')
    response = sns.publish(
        TopicArn='SNS_ARN',
        MessageGroupId='users',  # ONLY FOR FIFO QUEUES
        Message='message',
        MessageAttributes={
            'username': {
                'DataType': 'String',  # For SNS filtering DataType must be string
                'StringValue': username
            }
        }
    )
    return response
