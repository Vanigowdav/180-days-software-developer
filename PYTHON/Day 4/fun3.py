def hello_func(greeting, name):
	return '{} {}'.format(greeting, name)                
print(hello_func('Hi', 'Vani_Gowda'))


def hello_func(greeting, name = 'yes'):   #name as default value as yes 
	return '{} {}'.format(greeting, name)
print(hello_func('Hi'))                     # if i not declared second value here no error it take  default value



def hello_func(greeting, name = 'yes'):   #name as default value as yes 
	return '{} {}'.format(greeting, name)
print(hello_func('Hi' , 'Vani_Gowda'))


#here greeting is required parameter
# name is named parameter
#Here sequence of parameters are important    means you need to have first all required parameters should be written and then other parameters



#----------------Important2-------------
# def hello_func(name = 'yes', greeting):   #name as default value as yes #here you will error bcz of sequence param
# 	return '{} {}'.format(greeting, name)
# print(hello_func('Hi' , 'Vani_Gowda'))




#Positional arguments are knows as required parameters that can be called by 
#their position in the function call.

#Keywords arguments are arguments that can be called by their name.(eg: lastname)


def hello_func(greeting, goodbye, name = 'yes'):   #name as default value as yes 
	return '{} , {} --- {}'.format(greeting, name, goodbye)
print(hello_func('Hi' , 'Bye Bye' ,'Vani_Gowda'))



def hello_func(greeting, goodbye, lastname = 'ayyo', name = 'yes'):   #name as default value as yes 
	return '{} , {}_{} --- {}'.format(greeting, name, lastname, goodbye)
print(hello_func('Hi' , 'Bye Bye', name ='Vani', lastname = 'Gowdru'))
