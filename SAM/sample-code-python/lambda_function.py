import ptvsd
import json

from src.main_function import main_function

# Enable ptvsd on 0.0.0.0 address and on port 5890 that we'll connect later with our IDE
ptvsd.enable_attach(address=('0.0.0.0', 5890), redirect_output=True)
ptvsd.wait_for_attach()

def lambda_handler(event, context):
    
    print(event)
    main_function(event, context)
            
    return {
        'statusCode': 200,
        'body': json.dumps('Completed Lambda function!')
    }
