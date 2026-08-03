#Finding how many are even and how many are odd numbers present in a list.
my_list = [1,2,3,4,5,6,7,8,9]
even = []
odd = []
for i in my_list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Total number of even are :",len(even))
print("Total number of odd are:",len(odd))


#reverse a list 
my_list = ["apple", "orange", "banana", "mango"]
print(my_list[::-1])

    