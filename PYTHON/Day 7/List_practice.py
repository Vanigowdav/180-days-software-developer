#Finding sum and average of numbers from 1 to n

number = int(input("Enter a number:"))
number_list =[]
for i in range(1,number+1):
    number_list.append(i)
print(number_list)
print(sum(number_list))
print("avg:", sum(number_list) / len(number_list))


#Smallest and largest without using built in function 
my_list = [31, 28, 24, 23, 45]
largest = my_list[4]
smallest = my_list[0]
for i in my_list:
    if i <= smallest:
        smallest = i
    elif i >= largest:
        largest = i
print("Largest:", largest)
print("Smallest:", smallest)

