import os
import json

def handler(event, context):
    # validate inputs - AWS_REGION must be set in the operating system environment
    if 'AWS_REGION' not in os.environ:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "No configured region"}),
        }
    aws_region = os.environ['AWS_REGION']
    # if name is present in the input event include it in our response message
    if 'name' in event:
        message = f"Hello {event['name']}! From {aws_region}."
    else:
        message = f"Hello from {aws_region}."
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": message
        })
    }
