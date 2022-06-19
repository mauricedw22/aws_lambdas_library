import json
import boto3
import datetime
from decimal import Decimal
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):
    
    client = boto3.resource('dynamodb')
    
    table = client.Table('lambdaSample1')
    print(table.table_status)
    
    now = datetime.datetime.now()
    
    id_date = str(now)
    id_date2 = str(now + datetime.timedelta(seconds=5))
    
    print(id_date)
    print(id_date2)
    
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

    '''
    ########################################################################################
    
    # BATCH WRITES WITH FOR LOOP 
    with table.batch_writer() as batch:  
        for i in range(3):
          batch.put_item(
            Item={
                'mauricedw22':str(i),
                'tester':'Dougie Fresh ' + str(i),
                'status':'SUCCESS #' + str(i),
                'age':str(i*11)
            }    
          )
    '''

    '''
    ########################################################

    # QUERIES
    
    response = table.query(
        KeyConditionExpression=Key('mauricedw22').eq('1')
    )
    
    items = response['Items']
    
    print(items)

    '''


    
    return {
        'statusCode': 200,
        'body': 'Record deleted'
    }
