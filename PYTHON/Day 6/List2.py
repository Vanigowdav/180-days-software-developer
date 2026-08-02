#Unpacking values : Unpacking values from a list is a technique used to assign values from a list to new variable.
Coffee = ["Starbucks", 250, "Mall_of_asia"]
Coffee_brand , Price, Adress = Coffee
print("Coffee_brand:", Coffee_brand)
print("Cost of Price:", Price)
print("Location:",Adress)

#ValueError : If number of varibles on left side of assignment operator doesn't match the total number of items in the list.
# Coffee = ["Starbucks", 250, "Mall_of_asia"]
# Coffee_brand , Price, Adress, Flavor = Coffee



#Slice operator : Access portion of list 
desserts = ["Anicake", "Cookies","Ice cream","Pie"]
print(desserts[1:4])