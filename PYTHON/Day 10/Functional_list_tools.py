# Another way to create a list starting from an existing list 
# 1. filter() function: It is used to filter the elements of an iterable based on a condition.
    #  -> syntax: filter(function, iterable)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def is_even(num):
    return num % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(even_numbers)

# brief summary of filter() function:
# 1. When to use: Use the filter() function when you want to create a new list that contains only the elements of an existing list that meet a certain condition. 
# It is useful for filtering data based on specific criteria.
# 2. How it works: The filter() function takes two arguments: a function and an iterable (like a list).
# The function is applied to each element of the iterable, and only the elements for which the function returns True are included in the new list. 
# The result is an iterator, which can be converted to a list using the list() function.

# one program using filter() function to filter out list of female actors name from a list of actors names:
actors = ["Robert Downey Jr.", "Scarlett Johansson", "Chris Hemsworth", "Jennifer Lawrence", "Tom Holland", "Gal Gadot"]
def is_female_actor(name):  
    female_actors = ["Scarlett Johansson", "Jennifer Lawrence", "Gal Gadot"]
    return name in female_actors

female_actors = list(filter(is_female_actor, actors))
print(female_actors)