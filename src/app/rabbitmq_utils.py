import pika
from src.config.settings import RABBIT_MQ_HOST, RABBIT_MQ_LOGIN, RABBIT_MQ_PASSWORD

def get_rabbitmq_connection():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=RABBIT_MQ_HOST,
            credentials=pika.PlainCredentials(
                username=RABBIT_MQ_LOGIN,
                password=RABBIT_MQ_PASSWORD
            )
        )
    )
    return connection

def publish_message(queue_name: str, message: str):
    connection = get_rabbitmq_connection()
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_publish(exchange="", routing_key=queue_name, body=message)
    connection.close()