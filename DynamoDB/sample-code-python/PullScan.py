import boto3
import json

def lambda_handler(event=None, context=None):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('UsersLeaderboard')

    ##full scan
    response = table.scan(
    )
    items = response['Items']


    return {
        'statusCode': 200,
        'body': items
    }