import json

# import requests


def lambda_handler(event, context):
    
    #personId = event['queryStringParameters']['personId']

    return {
        "statusCode": 200,
        "body":
        #"body": json.dumps({
            """
            <html> 
            <p> Hello website Lambda </p> 
            <html>
            """,
            #"message": "hello world",
            #"personId": personId + " from Lambda" , 
            # "location": ip.text.replace("\n", "")
        #}),
        "headers": {"Content-Type": "text/html",},
    }
