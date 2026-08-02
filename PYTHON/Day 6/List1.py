#update value at particular index

kannda_kavi= ["Kuvempu", "Bendre", "Gopalakrishna Adiga", "D. R. Bendre", "K. S. Narasimhaswamy"]
print(kannda_kavi[0]) # Output: Kuvempu
kannda_kavi[3] = "Girsh Karnad" # update value at index 3
print(kannda_kavi) 

#Index Error : if you pass in an index that is out of bounds for the list.

# To remove an item from a list, we can use the remove() method. 
# This method removes the first occurrence of the specified value.
develpers = ["Vani", "Ravi", "Sudeep", "Yash", "Puneeth"]
develpers.remove("Sudeep") # remove "Sudeep" from the list
print(develpers) # Output: ['Vani', 'Ravi', 'Yash', 'Puneeth']


#To check an element is inside the list use " in " keyword
developers = ["Vani", "Anan", "Aura", "Giri","Surana"]
print("Vani" in developers)
print("Chethan" in developers)

#Nested list 
developers = ["Vani", "Anan", ["Aura", "Giri","Surana"]]
print(developers[2])
print(developers[2][1])

