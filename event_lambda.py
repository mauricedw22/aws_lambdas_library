import json
import boto3
import datetime

client = boto3.client('events')

# This Lambda sends an test event to a custom EventBridge event bus with content-based filter rule (rule match outputs to a receiver Lambda)

def lambda_handler(event, context):
    
    response = client.put_events(
        Entries=[
            {
                'Time': datetime.datetime.now(),
                'Source': 'Lambda Publish',
                'Resources': [],
                'DetailType': 'Custom event demo',
                'Detail': json.dumps(event),
                'EventBusName': 'arn:aws:events:us-east-1:330202998142:event-bus/custom-rule-demo',
                'TraceHeader': 'testdemo'
            }   
        ]
    )
    
    return response