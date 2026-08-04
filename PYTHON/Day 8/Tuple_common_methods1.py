# 3. sorted() - This method returns a new sorted list from the elements of the tuple.
my_tuple = (3, 1, 4, 2, 5)
sorted_tuple = sorted(my_tuple)
print("Sorted tuple:", sorted_tuple)  # Output: Sorted tuple: [1, 2, 3, 4, 5]

# If you want to sort the tuple in descending order, you can pass the reverse=True argument to the sorted() method.
sorted_tuple_desc = sorted(my_tuple, reverse=True)
print("Sorted tuple in descending order:", sorted_tuple_desc)  # Output: Sorted tuple in descending order: [5, 4, 3, 2, 1]

# using key parameter in sorted() method, we can sort the tuple based on a custom sorting criteria.
# For example, we can sort the tuple based on the absolute values of the elements.
my_tuple_with_negatives = (-3, 1, -4, 2, 5)
sorted_tuple_abs = sorted(my_tuple_with_negatives, key=abs)
print("Sorted tuple based on absolute values:", sorted_tuple_abs)  # Output: Sorted tuple based on absolute values: [1, 2, -3, -4, 5]
