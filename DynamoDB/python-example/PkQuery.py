import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event=None, context=None):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('UsersLeaderboard')

    ## pk query
    response = table.query(
        KeyConditionExpression=Key('id').eq(4)
        ## id(pk)가 4인 유저 조회
    )

    items = response['Items']

    return {
        'statusCode': 200,
        'body': items
    }