# Handling Exceptions
# Use a try-except block to handle exceptions and prevent program crashes.

# 1. Handling ZeroDivisionError:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Oops! You can't divide by zero.")


# 2. Handling Multiple Exceptions:

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input; please enter a number.")

# 3. Handling TypeError:
try:
    result = "string" + 10
except TypeError:
    print("Cannot add a string and an integer.")
