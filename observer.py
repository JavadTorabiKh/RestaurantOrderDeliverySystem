from abc import ABCMeta, abstractmethod
import pika
import uuid

# Subject


class Publisher:

    def __init__(self):
        self.__bike = []
        self.__latestFood = None

    def onlineBike(self, bike):
        self.__bike.append(bike)

    def Bikes(self):
        return [type(s).__name__ for s in self.__bike]

    def notifyForBike(self):
        for sub in self.__bike:
            sub.update()

    def addFoods(self, food):
        self.__latestFood = food

    def getFood(self):
        return self.__latestFood


# Observer
class Subscriber(metaclass=ABCMeta):

    @abstractmethod
    def update(self):
        pass


# ConcreteObserver
class EmailBike:

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.onlineBike(self)
    

    def update(self):
        fibonacci_rpc = RpcBike()
        food = self.publisher.getFood()
        print('food Message send .....')
        response = fibonacci_rpc.call(f'{food} baraye Mohhamad!!!')
        print(" [.] Got %r" % response)
        

# RPC RabbitMQ
class RpcBike(object):

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

        self.channel = self.connection.channel()
        

        
        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

        self.response = None
        self.corr_id = None

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, FoodMessage):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(FoodMessage))
        self.connection.process_data_events(time_limit=None)
        return self.response


if __name__ == '__main__':
    pub = Publisher()
    EmailBike(pub)

    pub.addFoods("PIZZA")
    pub.notifyForBike()
