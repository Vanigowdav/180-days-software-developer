# Attributes : Two Types attributes
# 1. Instance attribute : are unique to each object created from class 
# 2. class attribute : belong to the class itself and are shared by all instances of that class.

from ast import Attribute


class Dog:
    species = "French Bulldog"     # class attribute 
    def __init__(self, name):
        self.name = name           # Instance attribute
print(Dog.species)

# Note : We can access class attribute directly from class itself
                #  ------BUT-----
#        We need to create an object and pass it data first before we can access instance Attribute

dog1 = Dog("Jack")
print(dog1.name)
print(dog1.species)

dog2 = Dog("Tom")
print(dog2.name)
print(dog2.species)