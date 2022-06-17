import json
import boto3
from botocore.exceptions import ClientError

sns  = boto3.resource('sns')

def lambda_handler(event, context):
    
    print("AWS lambda and SNS trigger ");
    print(event);
    print(event['Records'][0]['Sns']['Message'])
    
    sns_published_message = event['Records'][0]['Sns']['Message']
    
    to_phone_number = '+12408865334'
    
    try:
        response = sns.meta.client.publish(
            PhoneNumber=to_phone_number,
            Message=sns_published_message
        )
        
        message_id = response['MessageId']
        print(message_id)
        
    except ClientError as error:
        print(error.response['Error']['Code'])
        print(error.response['Error']['Message'])
    
    else:
        return message_id