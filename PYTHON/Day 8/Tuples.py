# Tuples is a python data type that is used to store multiple items in a single variable.
# Tuples can store different data types and are immutable, meaning that once a tuple is created, its values cannot be changed.
developer = ("Vani", 23, "Python Developer", True)
print(developer)  # Output: ('Vani', 23, 'Python Developer', True)

#To access elements in a tuple, you can use indexing. Indexing starts at 0 for the first element, 1 for the second element, and so on.
print(developer[0])  # Output: Vani 
print(developer[1])  # Output: 23
print(developer[2])  # Output: Python Developer
print(developer[3])  # Output: True

#To access last element in a tuple, you can use negative indexing. The last element has an index of -1, the second-to-last element has an index of -2, and so on.
print(developer[-1])  # Output: True
print(developer[-2])  # Output: Python Developer

