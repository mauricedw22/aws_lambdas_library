import json

def lambda_handler(event, context):
    print("AWS lambda and SNS trigger ");
    print(event);
    print(event['Records'][0]['Sns']['Message'])