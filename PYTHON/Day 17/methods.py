# Methods : are functions inside a class.
class Dog:
    species = "French Bulldog" 
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def bark(self):
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old")
dog1 = Dog("jack", 3)
dog1.bark()
dog2 = Dog("Tom", 5)
dog2.bark()