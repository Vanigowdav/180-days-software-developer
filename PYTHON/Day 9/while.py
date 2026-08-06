# While loop repeat until the condition is False.

# 1. Counting with While Loop
count = 1
while count <= 5:
    print(count)
    count += 1                            # if you miss increment or decrement statement the code goes to infinite loop.


# 2. User Input Loop
user_input = ""
while user_input != "exit":
    user_input = input("Type 'exit' to stop: ")


# 3. Decrementing Loop
n = 5
while n > 0:
    print(n)
    n-= 1

# 4.Guessing secret_number
secret_number = 3
guess = 0
while guess!= secret_number:
    guess = int(input("Generate the number(1-5):"))
    if guess != secret_number:
        print("wrong! Try again")
    else:
        print("You got it")