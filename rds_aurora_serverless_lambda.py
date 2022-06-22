import json
import boto3

rds_client = boto3.client('rds-data')

db_name = 'auroraserverless1'
db_cluster_arn = 'arn:aws:rds:us-east-1:330202998142:cluster:aurora-serverless-1'
db_credentials_secrets_arn = '<SECRETS_ARN>'

def lambda_handler(event, context):
    response = execute_statement('SELECT * FROM auroraserverless1.Customers')
    return response['records']  # response['records'][0][2]['longValue'];
    
def execute_statement(sql):
    response = rds_client.execute_statement(
        secretArn=db_credentials_secrets_arn,
        database=db_name,
        resourceArn = db_cluster_arn,
        sql=sql
    )
    return response;