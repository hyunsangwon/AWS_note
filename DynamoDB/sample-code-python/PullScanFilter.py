import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event=None, context=None):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('UsersLeaderboard')

    ## pk,sort query
    response = table.scan(
        FilterExpression=Attr('TopScore').gt(50000)
    )

    items = response['Items']

    return {
        'statusCode': 200,
        'body': items
    }