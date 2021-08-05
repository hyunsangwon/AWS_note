import boto3
import traceback
from datetime import datetime
from src.move.outer_move_200213 import check_outer_move_event
from src.common.constants import *


def main_function(event, context):
    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            try:
                new_image = record['dynamodb']['NewImage']

                data_map = dict()

                data_map["euid"] = new_image['euid']['S']
                data_map["received_at_utc0"] = new_image['received_at_utc0']['S']
                data_map["packet_id"] = new_image['packet_id']['S']
                data_map["firmware_ver"] = new_image['firmware_ver']['S']
                data_map["cell_id"] = new_image['cell_id']['S']
                data_map["location_source"] = new_image['location_source']['S']

                data_map["lat"] = new_image['lat']['S']
                data_map["lng"] = new_image['lng']['S']

                data_map["packet_search_code"] = new_image['packet_search_code']['S']

                data_map["bank_srl"] = new_image['bank_srl']['S']
                data_map["branch_srl"] = new_image['branch_srl']['S']
                data_map["company_srl"] = new_image['company_srl']['S']
                data_map["warranty_srl"] = new_image['warranty_srl']['S']

                data_map["bank_nm"] = new_image['bank_nm']['S']
                data_map["branch_nm"] = new_image['branch_nm']['S']
                data_map["company_nm"] = new_image['company_nm']['S']
                data_map["warranty_nm"] = new_image['warranty_nm']['S']

                data_map["log_srl"] = new_image['log_srl']['S']

                data_map["is_detach_event"] = new_image['is_detach_event']['S']
                data_map["detach_event_check"] = new_image['detach_event_check']['S']

                data_map["mag"] = new_image['mag']['S']

                data_map = check_outer_move_event(data_map)

                dynamo_client = boto3.client(
                    'dynamodb', region_name='ap-northeast-2', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

                items = dict()
                for attr in data_map:
                    value = data_map[attr]
                    items[attr] = {"S": str(value)}
                dynamo_client.put_item(
                    TableName=EVENT_DIAGNOSIS_DB, Item=items)

                dynamo_client.update_item(
                    TableName=OUTER_MOVE_EVENT_CHECK_REQUEST_DB,
                    Key={"packet_search_code": {
                        "S": data_map["packet_search_code"]}},
                    UpdateExpression="set completed_at_utc0 = :r",
                    ExpressionAttributeValues={
                        ':r': {"S": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}}
                )
            except:
                dynamo_client = boto3.client(
                    'dynamodb', region_name='ap-northeast-2', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
                items = dict()
                items["packet_search_code"] = {
                    "S": str(data_map["packet_search_code"])}
                items["lambda"] = {"S": context.function_name}
                items["error"] = {"S": traceback.format_exc()}
                dynamo_client.put_item(TableName=ERROR_DB, Item=items)
