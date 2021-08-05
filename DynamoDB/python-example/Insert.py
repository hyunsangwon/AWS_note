import boto3
import json

def lambda_handler(event=None, context=None):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('UsersLeaderboard')

    ## insert put
    table.put_item(
        Item={
            'id': 8,
            'Week': '2019-11-27',
            'TopScore': 65335,
            'Name': 'sangwonHyun'
        }
    )

    return {
        'statusCode': 200
    }