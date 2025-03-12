import pika
import json


def deliver_order(ch, method, properties, body):
    order = json.loads(body)
    print(f" [x] Delivering order: {order}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='order_queue')

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='order_queue', on_message_callback=deliver_order)

print(" [x] Waiting for orders.")
channel.start_consuming()
