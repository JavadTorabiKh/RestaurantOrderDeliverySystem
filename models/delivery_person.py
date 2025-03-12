from .order import Observer


class DeliveryPerson(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, order):
        print(f"{self.name} has received a new order: {order}")
