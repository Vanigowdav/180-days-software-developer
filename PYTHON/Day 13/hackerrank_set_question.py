# NO idea! problem 
n, m = map(int, input("Enter the numbers for n and m: ").split())
arr = list(map(int, input("Enter the elements: ").split()))
assert len(arr) == n, f"Expected {n} elements in arr, got {len(arr)}"

A = set(map(int, input("Enter the elements: ").split()))
assert len(A) == m, f"Expected {m} elements in A, got {len(A)}"

B = set(map(int, input("Enter the elements: ").split()))

happiness = 0
for i in arr:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
print(happiness)


# learnt about assert
# syntax: assert <condition>, <message> 
    #    - If the condition is True → nothing happens, the program just continues to the next line.
    #    - If the condition is False → Python raises an AssertionError, using the message as the error text, and the program stops right there (unless you catch the exception with try/except).
