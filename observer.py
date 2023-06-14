from abc import ABCMeta, abstractmethod
import pika

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
    
    def on_request(self,ch, method, props ,body):
        message = self.publisher.getFood()    
        print(" [.] message is", message)
        ch.basic_publish(
            exchange='',
            routing_key=props.reply_to,
            properties=pika.BasicProperties(correlation_id=props.correlation_id),
            body=message)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def update(self):
        
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='rpc_queue')
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='rpc_queue', on_message_callback=self.on_request)
        print(" [x] Awaiting RPC requests")
        channel.start_consuming()
        

if __name__ == '__main__':
    pub = Publisher()
    EmailBike(pub)

    pub.addFoods("PIZZA")
    pub.notifyForBike()
    print("\nBikess: ", pub.Bikes)
