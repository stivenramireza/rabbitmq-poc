import pika

from logger import logger


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

    logger.info("[x] Sent 'Hello World!'")
    connection.close()


if __name__ == '__main__':
    main()
