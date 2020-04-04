import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event=None, context=None):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('UsersLeaderboard')

    ## pk,sort,filter query
    response = table.query(
        KeyConditionExpression=Key('id').eq(4)&Key('Week').between('2019-11-23', '2019-11-27'),
        FilterExpression=Attr('TopScore').gt(50000),
        Limit=10
    )

    items = response['Items']

    return {
        'statusCode': 200,
        'body': items
    }