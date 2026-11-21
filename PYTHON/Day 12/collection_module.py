# Fruits problem : When the user input same fruit again it adds it price to the repeated fruit
# 1.OrderedDict
from collections import OrderedDict
from typing import DefaultDict
n = int(input("enter a number of times the loop to be run: "))
fruits = OrderedDict()
for i in range(n):
    word = input("Enter a name and price of fruit: ").split()
    name = " ".join(word[:-1])
    price = int(word[-1])
    fruits[name] = fruits.get(name, 0) + price
print(fruits)

# 2.DefaultDict
# There is two dictionaries it need to return the position of value in A ,  if and only if the value of B is also in  present A. else -1
from collections import defaultdict
n, m = map(int, (input("Enter a value for n and m:").split()))
grp_a = defaultdict(list)
for i in range(n):
    value = input("Enter a word to insert in grp_a: ")
    grp_a[value].append(i + 1)
for j in range(m):
    val = input("Enter a word to insert in grp_b: ")
    grp_b = grp_a.get(val)
    print(" ".join(map(str, grp_b)) if grp_b else -1)


# 3.Counter
# Count how many times each element appears 
from collections import Counter
numbers = [1, 2, 2, 4, 5, 3, 3, 2, 6, 7, 8, 6, 8]
result = Counter(numbers)
print(result)


