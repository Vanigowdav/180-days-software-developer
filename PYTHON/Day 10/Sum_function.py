# Sum() function : used to get the sum from iterable like list or tuple 
# syntax: sum(iterable, start=0)   here start is positional argument and it is optional.

numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total)


numbers = [5, 10, 15, 20]
total = sum(numbers, 10)    # here python does : 10 + (5+10+15+20) = 60
print(total)
