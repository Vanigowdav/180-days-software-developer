# Uppercase Converison 
names = ["vanigowda", "pranavgowda", "ridugowda", "ananyagowda", "virugowda"]
name_conversion = [name.upper() for name in names]
print(name_conversion)

# want to print one by one 
for name in name_conversion:
    print(name)


#want to give sperate first and last name 
for name in name_conversion:
    index = name.find("GOWDA")
    first = name[:index]
    last = name[index:]
    print(f"{first} {last}")

