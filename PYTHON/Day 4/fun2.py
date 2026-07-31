#dummy fuction you are not going to do anything inside the function use pass word

def func():
	pass

#calling fucn
print(func())   #print none 

print(func)   #return refernces for func


def hello_func():
	return 'Hello Learners'
hello_func()           #its print nothing bcs i have  not used print here


def hello_func():
	return 'Hello Learners'
print(hello_func())     #return hello learners

# -------------------or----------------

def hello_func():
	return 'Hello Learners'
string = hello_func()
print(string)

#----Important----------
def hello_func(name):                      #giving parameter
	return 'Hello , {}'.format(name)

print(hello_func())       #if i do not give anything here error will come  i.e missing 1 required positional argument



