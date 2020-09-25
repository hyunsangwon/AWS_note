import ptvsd
from src.handler_function import handler_function


# Enable ptvsd on 0.0.0.0 address and on port 5890 that we'll connect later with our IDE
ptvsd.enable_attach(address=('0.0.0.0', 5890), redirect_output=True)
ptvsd.wait_for_attach()

def lambda_handler(event, context):
    handler_function(event, context)