# List comprehension are concise way to create lists in Python.
# It provides a shorter syntax when you want to create a new list based on the values of an existing list.
# syntax: [expression for item in iterable if condition == True]

even_numbers = [x for x in range(1,20) if x % 2 == 0]
print(even_numbers)


#Conditional list comprehension:
# It allows you to create a new list based on a condition applied to the elements of an existing list.
names = ["Alice", "Bob", "Charlie", "David"]
long_names = [name for name in names if len(name) > 4]
print(long_names)


flavors = ["chocolate", "vanilla", "strawberry", "mint"]
# Create a new list with the lengths of each flavor 
flavor_lengths = [len(flavor) for flavor in flavors]
print(flavor_lengths)


positive_numbers = [x for x in range(-10, 11) if x > 0]
print(positive_numbers)

# conditional list comprehension and list comprehension with multiple conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Create a new list with even numbers that are greater than 5
even_numbers_greater_than_5 = [x for x in numbers if x % 2 == 0 and x > 5]
print(even_numbers_greater_than_5)


# Example of nested list comprehension:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)
