import pika


def fibonacci(message):
    return message


def on_request(ch, method, props, body):
    message = body
    print(" [.] message is", message)
    response = fibonacci(message)
    ch.basic_publish(
        exchange='',
        routing_key=props.reply_to,
        properties=pika.BasicProperties(correlation_id=props.correlation_id),
        body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)
print(" [x] Awaiting RPC requests")
channel.start_consuming()


# import pymongo


# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

#     def register(self):

#         db = self.client["microService"]

#         user_data = {"name": self.name, "email": self.email}

#         bikes = db["bike"]

#         result = bikes.insert_one(user_data)

#         print(result.inserted_id)


# user = User("metti", "metti@gmail.com")
# user.register()
