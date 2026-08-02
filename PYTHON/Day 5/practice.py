counter = 0
def add_numbers(a, b):
    global counter
    counter += 1
    result = a + b
    print(f"Result: {result}, Counter: {counter}")


#Call the function multiple times
add_numbers(2, 3)
add_numbers(7, 8)
add_numbers(10, 5)

print(f"Total function calls: {counter}")
print(f"Final Counter Value: {counter}")