import json
import urllib
import boto3

def lambda_handler(event, context):
    # S3 ObjectCreate trigger on a lambda with simple json file processing
    
    s3 = boto3.client('s3')
    
    # Get bucket name
    bucket = event['Records'][0]['s3']['bucket']['name']

    # Get the file/key name from s3
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    try:
        # fetch file from s3
        response = s3.get_object(Bucket=bucket, Key=key)
        
        # Deserialize the file's contents
        text = response['Body'].read().decode()
        data = json.loads(text)
        
        # Print the content
        print(data)
        
        # Parse and print the sample transaction json data
        transactions = data['transactions']
        for record in transactions:
            print(record['transType'])
        return 'Success!'
        
    except Exception as e:
        print(e)
        raise e