import pika
import json
import uuid

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(
    exchange='telemetry',
    exchange_type='direct'
)
queue = channel.queue_declare('telemetry_notify')
queue_name = queue.method.queue

channel.queue_bind(
    exchange="telemetry",
    queue=queue_name,
    routing_key='telemetry.notify'
)

