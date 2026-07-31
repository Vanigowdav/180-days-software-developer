# funcparam2
# *args for the arbitrary number of positional arguments 
# **kwargs for the arbitrary number of keyword arguments

#TYPE 1
# def func(*args, **kwargs):
# 	print(args)
# 	print(kwargs)

# func('COA', 'OS', name= 'Vani', age = 25)

#TYPE 2
def func(*args, **kwargs):
	print(args)
	print(kwargs)

courses = ['coa', 'os']
info = {'name': 'vani', 'age':25}    #different ouput check out
func(courses,info)



def func(*args, **kwargs):
	print(args)
	print(kwargs)

courses = ['coa', 'os']                  #same output as first one 
info = {'name': 'vani', 'age':25}
func(*courses, **info)