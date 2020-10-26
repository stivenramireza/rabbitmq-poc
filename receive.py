import os
import pika
import sys

from logger import logger


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        logger.info(" [x] Received %r" % body)

    channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)

    logger.info(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logger.error('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
