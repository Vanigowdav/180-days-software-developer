# Loops : Used to repeat a block of code for set of number of times.
# for loop : used to repeat a code at specific times
# while loop : repeat until the condition is false.

# For loops:A for loop is used when you know in advance how many times you want to repeat a block of
# code.

# 1. Iterating over list 
fruits = ["mango", "apple", "orange", "gauva", "grapes"]
for fruit in fruits:
    print(fruits)


# 2. iterate through string:
for char in "vani":
    print(char)

# 3. Range Loop
for i in range(5):
    print(i)


#4. Nested for loops:
categories = ["Fruit", "Vegetable"]
foods = ["Apple", "Carrot", "Banana"]
for category in categories:
    for food in foods:
        print(category,food)