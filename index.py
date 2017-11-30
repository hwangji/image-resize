import json
import datetime


def handler(event, context):
    current_time = datetime.datetime.now() + timedelta(hours=9)
    body = {
        "message": "The time in Korea is " + str(current_time)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response