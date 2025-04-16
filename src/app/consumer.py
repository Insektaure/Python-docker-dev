import pika
from src.config.settings import RABBIT_MQ_HOST, RABBIT_MQ_LOGIN, RABBIT_MQ_PASSWORD

def callback(ch, method, properties, body):
    print(f"Received message: {body.decode()}")

def consume_messages(queue_name: str):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=RABBIT_MQ_HOST,
            credentials=pika.PlainCredentials(
                username=RABBIT_MQ_LOGIN,
                password=RABBIT_MQ_PASSWORD
            )
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    print(f"Waiting for messages in queue '{queue_name}'. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == "__main__":
    consume_messages("default_queue")