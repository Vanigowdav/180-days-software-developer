# Common elements
my_list = [1, 2, 4, 5, 7, 8, 10, 22]
your_list = [2, 4, 8, 10, 22, 3, 6, 9]
common_list  = [num for num in (my_list) if num in your_list]
print(common_list)