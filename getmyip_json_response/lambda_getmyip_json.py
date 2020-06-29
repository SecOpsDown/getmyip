import json

def lambda_handler(event, context):
    
    headers = event['context']
    data = {
        'My IP': headers['source-ip'],
        'My user agent': headers['user-agent'],
        'Requested URI': '/' + headers['stage'] + headers['resource-path'],
        'Method used': headers['http-method']
    }
    return_message = {
        'statusCode': 200,
        'body': data
    }
    return return_message