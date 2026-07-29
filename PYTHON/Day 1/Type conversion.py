#Type conversion 
# str to int
str_num = "10"
int_num = int(str_num)
print("String to Integer:",int_num)
print(type(int_num))
print(type(str_num))


# int to str 
int_num2 = 20
str_num2 = str(int_num2)   
print("Integer to String:",str_num2)
print(type(int_num2))
print(type(str_num2))

# int to float
int_num3 = 30
float_num = float(int_num3)
print("Integer to Float:",float_num)
print(type(int_num3))
print(type(float_num))

# float to int
float_num2 = 40.5
int_num4 = int(float_num2)
print("Float to Integer:",int_num4)
print(type(float_num2))
print(type(int_num4))

#---------------------Simple Bill Program-----------------------
price = float(input("Enter the price of the item:"))
quantity = int(input("Enter the quantity of the item:"))
discount = float(input("Enter the discount percentage:"))
subtotal = price * quantity
discount_amount = subtotal * (discount / 100)
total = subtotal - discount_amount
print("Subtotal: $", subtotal)
print("Discount Amount: $", discount_amount)
print("Total: $", total)

