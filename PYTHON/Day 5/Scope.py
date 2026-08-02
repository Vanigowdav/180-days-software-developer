# #Scope is a region of the program where a defined variable can have its existence and beyond that variable 
# # cannot be accessed. In python, there are two types of scope: Local and  Global.

# # Local scope : Variables defined inside a function are in the local scope of that function and can only be accessed inside that function.

# #example 1:
def my_func():
    x = 10
    print(x) # x is accessible here 

my_func() # here output will be 10
#print(x) # x is not accessible here, will raise an error 

#example 2:
def func1():
    x = 40
    def func2():
        print(x) #  x is accessible here because func2 is nested inside func1
    func2()
func1() # here output will be 40
#print(x) # x is not accessible here, will raise an error


# 2.Global scope : Variables defined outside a function are in the global scope and can be accessed inside or 
# outside of a function.

#example 1:
my_var = 20 # my_var is in global scope
def show_var():
    print(my_var) # my_var is accessible here

show_var() # here output will be 20
#print(my_var) # my_var is accessible here

# To make a locally scoped variable global, we can use the global keyword. 
# This is useful when we want to modify a global variable inside a function.

# my_var = 30 # my_var is in global scope
def modify_var():
    global my_var # declare my_var as global
    my_var = 40 # modify the global variable
    print(my_var) # my_var is accessible here
modify_var() # here output will be 40
print(my_var) # my_var is accessible here, output will be 40

# #to make a variable local to a function, we can use the nonlocal keyword.
def outer_func():
    msg = "Hello" # msg is in outer_func's local scope
    def inner_func():
        nonlocal msg # declare msg as nonlocal
        msg = "Hi" # modify the nonlocal variable
        print(msg) # msg is accessible here
    inner_func() # here output will be Hi
outer_func() # here output will be Hi




