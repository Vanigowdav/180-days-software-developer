number = int(input("Enter a number: "))
if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")
if number > 0:
    for i in range(1, number + 1):
        print(i)
