import pymongo


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

    def register(self):

        db = self.client["microService"]

        user_data = {"name": self.name, "email": self.email}

        bikes = db["bike"]

        result = bikes.insert_one(user_data)

        print(result.inserted_id)


user = User("metti", "metti@gmail.com")
user.register()
