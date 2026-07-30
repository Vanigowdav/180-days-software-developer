#Strings are sequence of characters wrapped in single or double quotes.
#String is immutable datatype means once declared cannot modify or alter.
#Multi line string using trople double quotes or single quotes.
# eg my_str = """Multiple strings"""

# 1.in operator :used to check if string contains one or more character which return boolean value.
my_str_1 = "Hello World"
print("Hello" in my_str_1)

#2. len - length of string : used to get the lenth of the string 
my_str_2 = "My name is Anan"              #note : count space as one string 
print(len(my_str_2))

#Indexing : used to access each character in a string, using sqaure brackets[]. Indexing starts from zero.
my_str_3 = "Welcome To Python World"
print(my_str_3[0])
print(my_str_3[7])

#negative indexing : indexing from last character but starts from -1 , second last character with -2 and so on 
my_str_4 = "Vaishnavi"
print(my_str_4[-2])

#Strings are immutable but can reassign a different string to a variable 
my_str_5 = "hi"
my_str_5 = "Hello"
print(my_str_5)    #here last updated recent string printed  ie Hello 


#String modification is not possible 
my_str = "Welcome"
my_str[0] = "s"    #here typeError 
print(my_str)

