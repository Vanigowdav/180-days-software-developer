# Functions in python are reusable code that when you call them 
# Built-in Functions 
# print() : used to output the data 
# input(): used to get the prompt from the user 
# int(): convert number, boolean, and numeric strings to integer .

#To write own function
# ----------SYNTAX----------------------
# def (keyword) name of function():
def hello():
    print("Hello", "world") 
hello()                         #calling a function 

# type 1 : no parameter, no return 
def greet():
    print("Hello")

greet()     #calling function



#type 2 : parameter, no return 
def greet(name):
    print("hello", name)


greet("anan")


# type 3 : no parameter, return 
def greet():
    return "hello"


y = greet()
print(y)


#type 4: parameter , return 
def greet(name):
    return "hello", name

y = greet("anan")
print(y)
