# Lambda functions : Used when you're dealing with single inline expression consider using lambda function.
# syntax : lambda arguments: expression
# Use lambda function works with higher order function like map and fileter().

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x:x % 2 == 0, numbers))
print(even_numbers)

# map() with lambda
numbers = [1, 2, 3, 4, 5]

# Square each number
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# map and filter together 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get even numbers, then double them
result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # [4, 8, 12, 16, 20]
