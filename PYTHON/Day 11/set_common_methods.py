# 1. Adding elements:
my_set1 = {1, 2, 3, "apple", "mango", 3, 4, 2}
my_set1.add(6)
print(my_set1)

# 2. Remove() or discard() : To remove an element from the set
# remove method will raise keyError if element is not found but discard will not 
my_set1.remove("apple")
print(my_set1)
my_set1.discard("banana")
print(my_set1)

# 3. clear ()
my_set1.clear()
print(my_set1)
