# example 1:
if 5 > 3:
    print("5 is greater than 3")
else:
    print("5 is not greater than 3")

# example 2:
if 5 == 5 and 10 > 5:
    print("Both conditions are true")
elif 5 != 5 and 10 > 5:
    print("First condition is false and second condition is true")
else:
    print("Both conditions are false")


#example 3:
savitha = "Mango"
kavi = "Banana"
count_mango = 5
count_banana = 3
if savitha == "Mango" and kavi == "Banana":
    print("Savitha likes Mango and Kavi likes Banana")
elif savitha == "Mango" and kavi != "Banana":
    print("Savitha likes Mango and Kavi does not like Banana")
elif savitha != "Mango" and kavi == "Banana":
    print("Savitha does not like Mango and Kavi likes Banana")
else:
    print("Savitha does not like Mango and Kavi does not like Banana")      


#example 2:
shop = "Flower Shop"
has_sunflower = True
if shop == "Flower Shop" and has_sunflower:
    print("The shop is a Flower Shop and it has Sunflowers")
elif shop == "Flower Shop" and not has_sunflower:
    print("The shop is a Flower Shop but it does not have Sunflowers")
elif shop != "Flower Shop" and has_sunflower:
    print("The shop is not a Flower Shop but it has Sunflowers")
else:
    print("The shop is not a Flower Shop and it does not have Sunflowers")
