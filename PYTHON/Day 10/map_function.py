# map() function : used to apply a function to all the items in an iterable (like a list) and return a map object (which is an iterator).
# syntax: map(function, iterable)
numbers = [1, 2, 3, 4, 5]
def square(num):    
    return num ** 2

squared_numbers = list(map(square, numbers))
print(squared_numbers)

#map fucntion are used to apply a function on each item of an iterable and 
# return a new iterable with the results.

# Difference between map() and filter() function:
# 1. Purpose: The map() function is used to transform or modify each element of an iterable
# , while the filter() function is used to select elements from an iterable based on a condition.
# 2. Return Value: The map() function returns a map object (which is an iterator) containing the transformed elements, 
# while the filter() function returns a filter object (which is also an iterator) containing only the elements that satisfy the condition.
# 3. Function Application: The map() function applies a given function to each element of the iterable,
# while the filter() function applies a given function to each element of the iterable and includes only those elements for which the function returns True.
# 4. Use Cases: Use the map() function when you want to perform a transformation on each element of an iterable,
# and use the filter() function when you want to select elements from an iterable based on a specific condition.
# 5. Example:

# Using map() to covert celsius to fahrenheit
celsius = [0, 10, 20, 30, 40]
def to_fahrenheit(temp):
    return(temp * 9/5) + 32

fahreheit = list(map(to_fahrenheit, celsius))
print(fahreheit)

