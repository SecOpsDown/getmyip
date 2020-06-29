import json

def lambda_handler(event, context):
    
    headers = event['context']
    response_title = '<html><head><title>Client INFO</title></head>'
    response_body = '<body><h1>IP ADDRESS: ' + headers['source-ip'] +  '</h1></body></html>'
    response_html = response_title + response_body
    response = {
            'statusCode': 200,
            'body': response_html,
            'headers': {
                'Content-Type': 'text/html',
                }
            }
    return response