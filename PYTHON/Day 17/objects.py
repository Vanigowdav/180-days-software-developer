# Creating object from a class 
# Syntax
# object1 = ClassName(attribute1, attribute2)

class Dog:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    # def bark(self):
    #     print(f"{self.name.upper()} says woof woof!")
dog1 = Dog("jack", 3)
print(dog1.name)

# call any of the methods defined in class from each object.
# syntax:
#  object1.method_name()

class Dog:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def bark(self):
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old")
dog1 = Dog("jack", 3)
dog1.bark()
