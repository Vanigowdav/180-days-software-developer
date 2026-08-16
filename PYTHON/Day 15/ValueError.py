# ValueError

try:
    number = int("abc")
except ValueError:
    print("Invalid input; please enter a number.")