# 1. count() - This method returns the number of times a specified value appears in the tuple.
my_tuple = (1, 2, 3, 4, 5, 1, 2, 1)
count_1 = my_tuple.count(1)
print("Count of 1 in the tuple:", count_1)  # Output: Count of 1 in the tuple: 3  

#If no argument is passed into count() method, python will raise a TypeError. 
# The count() method requires a single argument, which is the value to be counted in the tuple.


# --------Important Note-------------------------------
#If specified value is not found in the tuple, the count() method will return 0.


# 2. index() - This method returns the index of the first occurrence of a specified value in the tuple. 
# If the value is not found, it raises a ValueError.
my_tuple = (1, 2, 3, 4, 5, 1, 2, 1)
index_1 = my_tuple.index(1) 
print("Index of first occurrence of 1 in the tuple:", index_1)  # Output: Index of first occurrence of 1 in the tuple: 0

# We can pass start and end parameters to the index() method to specify a range within which to search for the value. 
# The start parameter is the index to start searching from, and the end parameter is the index to stop searching at (exclusive).
index_1_range = my_tuple.index(1, 2, 6)  # Search for 1 between indices 2 and 6 (exclusive)
print("Index of first occurrence of 1 in the tuple between indices 2 and 6:", index_1_range)  # Output: Index of first occurrence of 1 in the tuple between indices 2 and 6: 5
