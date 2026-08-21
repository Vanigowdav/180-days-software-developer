class Database:
    def __init__(self):
        self.__storage = {}
    def save_data(self, key, value):
        self.__storage[key] = value
        print(f"Data saved for {key}")

    def get_data(self, key):
        return self.__storage.get(key, "NO data found")

db = Database()
db.save_data("user_101", {"name": "Raj", "age": 30})
print(db.get_data("user_101"))



# The user can store and retrieve data without needing to know the storage details.





