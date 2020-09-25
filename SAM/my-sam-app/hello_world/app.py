import json

def lambda_handler(event, context):
  
    print('sangwon team ground bjj')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')

    }