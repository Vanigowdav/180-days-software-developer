#Concatenation of strings : combining multiple strings together with (+) operator 
my_str = "Anuvaad"
my_str1 = "Gowda"
print(my_str + my_str1)   #here output : AnuvaadGowda observe there is no space between firstname and lastname add space(' ') between the strings.
print(my_str + ' '+ my_str1)


#Note : If you trying to concate a string with a number TypeError will occur 
name = "Eman"
age = 24
# name_and_age = name + age
# print(name_and_age)
# so here convert the other datatypes like integers into strings when you want to concate them 
name_and_age = name + ' ' +str(age)
print(name_and_age)

#Auguement operator(+=): perform concatenation and assignment in one step 
name = "Eman"
age = 23
name_and_age = name 
name_and_age += str(age)
print(name_and_age)