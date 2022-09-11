import datetime

import pika
import json
import uuid

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


def generate_telemetry():
    now = datetime.datetime.now()
    return {
        'id': 'smart-light-01',
        'status': 'ON',
        'time': now.strftime("%d/%m/%Y %H:%M:%S")
    }

payload = generate_telemetry()

channel.basic_publish(
    exchange="telemetry",
    routing_key="telemetry.notify",
    body=json.dumps(payload)
)

print('Sent payload {}'.format(str(payload)))