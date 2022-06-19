import json
import boto3
import datetime

def lambda_handler(event, context):
    
    client = boto3.resource('dynamodb')
    
    table = client.Table('lambdaSample1')
    print(table.table_status)
    
    id_date = str(datetime.datetime.now())
    print(id_date)
    
    '''
    ###################
    # DynamoDB PUT_item
    obj = {'mauricedw22': id_date, 'tester':'Maurice da Best', 'status':'success', 'age':33}
    
    table.put_item(Item=obj)
    
    ###################
    # DynamoDb GET_item
    
    dynamoData = table.get_item(
        Key={
            'mauricedw22':'2022-06-15 23:17:08.570746'
        }
    )
    
    
    item = dynamoData['Item']
    print('Previous db item: ', item)
    '''
    
    ########################################################################################
    
    '''
    ######################
    # DynamoDB UPDATE_item
    
    table.update_item(
        Key={
            'mauricedw22':'2022-06-15 23:35:10.880650'
        },
        UpdateExpression='SET tester = :val1',
        ExpressionAttributeValues={
            ':val1':'Mauricedw22 is da Bestest'
        }
    )
    
    ###################
    # DynamoDB get_item
    
    updatedItem = table.get_item(
        Key={
            'mauricedw22':'2022-06-15 23:35:10.880650'
        }    
    )
    
    item = updatedItem['Item']
    print(item)
    '''
    
    ########################################################################################
    
    '''
    ######################
    # DynamoDB DELETE_item
    table.delete_item (
        Key={
            'mauricedw22':'2022-06-15 23:17:08.570746'
        }    
    )
    '''

    ###################################################    
    
    '''
    # BATCH WRITES example
    
    obj2 = {'mauricedw22':id_date,'tester':'Dougie','status':'SUCCESS','age':'Prime'}
    
    obj3 = {'mauricedw22':id_date2,'tester':'Dougie','status':'SUCCESS','age':Decimal(33.5)}
    
    with table.batch_writer() as batch: # overwrite_by_pkeys=['partition_key','sort_key'] -> for de-Duplicating
        batch.put_item(Item=obj2)
        batch.put_item(Item=obj3)
    '''
    
    ########################################################################################
    
    return {
        'statusCode': 200,
        'body': 'Record deleted'
    }
