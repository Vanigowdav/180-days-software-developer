# We can raise exceptions manually using the raise keyword to indicate an error condition.

# 1. Raising a ValueError

from tabnanny import check


def check_positive(number):
    if number < 0:
        raise ValueError("Negative numbers are not allowed")
    return number

try:
    print(check_positive(-5))
except ValueError as e:
    print(e)