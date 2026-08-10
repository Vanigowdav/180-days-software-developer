# Python Module : A module is a file containing Python code, including functions, classes, and variables.
# To use a module, you need to import it using the 
#   -import module_name statement
#   -To call a function from the module use dot notation , with the name of module followed by name of the function.

# 1. math module : used to perform more complex mathematical operations.
import math 

# Calculate the square roo of 16
result = math.sqrt(16)
print(result)

# 2. random module: used for generating random numbers.
import random

#Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print(random_number)

# 3. statistics module 
import statistics

# Calculate the mean of a list of numbers
data = [1, 2, 3, 4, 5]
mean_value = statistics.mean(data)
print(mean_value)

# 4. datetime module : used for working with dates and times in python.
import datetime

#Get the current date and time 
current_time = datetime.datetime.now()
print(current_time)

# 5. os module : The os module in Python is a built-in library that lets your code interact with the operating system — 
#                things like files, directories, environment variables, and processes
import os 

# Get the current working directory
current_directory = os.getcwd()
print(current_directory)
