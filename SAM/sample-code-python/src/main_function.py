import boto3
import traceback
from datetime import datetime
from src.common.constants import *


def main_function(event, context):
    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            new_image = record['dynamodb']['NewImage']
            data_map = dict()
            try:
                data_map["name"] = new_image['name']['S']
                data_map["age"] = new_image['age']['N']
            except:
                dynamo_client = boto3.client('dynamodb', region_name='ap-northeast-2')
                items = dict()
                items["lambda"] = {"S": context.function_name}
                items["error"] = {"S": traceback.format_exc()}
                dynamo_client.put_item(TableName=ERROR_DB, Item=items)