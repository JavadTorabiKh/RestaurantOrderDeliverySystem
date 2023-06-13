from abc import ABCMeta, abstractmethod


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
        return "food : ", self.__latestFood


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
        print(type(self).__name__, self.publisher.getFood())


if __name__ == '__main__':
    pub = Publisher()
    EmailBike(pub)

    pub.addFoods("PIZZA")
    pub.notifyForBike()
    print("\nBikess: ", pub.Bikes)
