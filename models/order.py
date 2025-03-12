class Observer:
    def update(self, order):
        raise NotImplementedError("Subclasses should implement this method.")


class Order:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, order_details):
        for observer in self._observers:
            observer.update(order_details)
