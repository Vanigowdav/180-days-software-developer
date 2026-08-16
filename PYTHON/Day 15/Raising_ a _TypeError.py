# 2. Raising a TypeError
def add_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both argumemnts must be integers.")
    return a + b

try:
    print(add_numbers(5, "10"))
except TypeError as e:
    print(e)