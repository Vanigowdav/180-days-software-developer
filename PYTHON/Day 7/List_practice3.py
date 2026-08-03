#Check whether an given element present in list are not 
my_list = [250, 455, 650, 345, 903, 643, 543, 632, 124, 452]
num = int(input("Enter a number to search:"))
if num in my_list:
    print("Found")
else:
    print("Not Found")