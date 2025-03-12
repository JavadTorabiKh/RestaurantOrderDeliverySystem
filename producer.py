import pika
import json
from models.order import Order
from models.delivery_person import DeliveryPerson


class OrderSystem(Order):
    def send_order(self, order_details):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='order_queue')

        message = json.dumps(order_details)
        channel.basic_publish(
            exchange='', routing_key='order_queue', body=message)
        print(f" [x] Sent order: {order_details}")
        connection.close()

        self.notify_observers(order_details)


order_system = OrderSystem()
delivery_person_1 = DeliveryPerson("Ali")
delivery_person_2 = DeliveryPerson("Sara")

order_system.register_observer(delivery_person_1)
order_system.register_observer(delivery_person_2)

order = {
    'restaurant_id': '123',
    'order_id': 'abc123',
    'delivery_address': 'Tehran, Iran',
    'items': ['Pizza', 'Salad']
}
order_system.send_order(order)
