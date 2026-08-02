# 1. append(): used to add item to the end of list
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers)

# 2. append can also used to add one list to another list 
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]
numbers.append(even_numbers)
print(numbers) 
#here another list append as list 

#3. extend(): To add all the individual numbers to list at the end use " extend()" method
numbers = [1, 2, 3, 4, 5]
odd_numbers = [7, 9, 11]
numbers.extend(odd_numbers)
print(numbers)

# 4. insert() : used to insert an element at a specific index in a list 
# This method accepts two arguments : index, new item want to insert
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)
print(numbers) 

# 5. pop() : used to remove an element at a specific index
numbers.pop(2)
print(numbers)    #delete the element at index 2

#------Important-----
# If we don't specify an element for the pop method then last elemt is removed
numbers = [1, 2, 3, 4, 5, 6, 7]
numbers.pop()
print(numbers)

#6. Sorted()
Collections = ["Earrings","Dress","Chains","Makeup kit"]
Sorted_Collections = sorted(Collections)
print(Sorted_Collections)

# 7. reverse(): used to reverse a list 
numbers.reverse()
print(numbers)




