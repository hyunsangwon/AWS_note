import json

# DynamoDB에서 Insert 발생시 실행하는 프로세스 코드
def lambda_handler(event, context):
    # TODO implement
    for record in event['Records']:
        if record['eventName'] == 'INSERT':
            
            name = record['dynamodb']['NewImage']['name']['S']
            print('what is your name ?' , name)
            
            # Insert가 발생한 DynamoDB Table 이름
            ddbARN = record['eventSourceARN']
            dbTableName = ddbARN.split(':')[5].split('/')[1]
            
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
