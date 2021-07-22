import requests
import json

def sendTextMessage(message,contactnumber):

    url = "https://www.fast2sms.com/dev/bulkV2"

    payload = "sender_id=TXTIND&message="+message+"&route=v3&numbers="+contactnumber
    headers = {
        'authorization': "0Hh2IbJFOnTZltjYALm6q3Gu9RyezDXQaCcogskENpvBVd1x5ijUs106qOeMu8CL5grw3lWoSPxvT2yd",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    data = json.loads(response.text)
    return data['return']