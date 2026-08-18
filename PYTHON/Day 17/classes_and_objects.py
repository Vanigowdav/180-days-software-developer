# class is like a blueprint or template used to create objects.
# To create  class :
#     -use class keyword
#     -name of the class
#     -followed by colon

# within in class , you can add an initializer along with attributes and methods.

# Attributes : are like varibles within the class and are used to store data.
# Methods: are functions defined within a class and are the actions objects created with a class can perform.

# syntax:
class ClassName:
    def __init__(self,name, age):
        self.name = name 
        self.age = age 
    def sample_method(self):
        print(self.name.upper())

