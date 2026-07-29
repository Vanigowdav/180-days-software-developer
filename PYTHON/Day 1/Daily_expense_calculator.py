print("-------Daily Expense Calculator-------")
Breakfast = float(input("Enter the amount spent on breakfast: "))
Lunch = float(input("Enter the amount spent on lunch: "))
Dinner = float(input("Enter the amount spent on dinner: "))
Snacks = float(input("Enter the amount spent on snacks: "))
Total_expense = Breakfast + Lunch + Dinner + Snacks
print("Total Expense for the day: $", Total_expense)
Total_money = float(input("Enter your total money for the day: "))
Remains = Total_money - Total_expense
print("Remaining Money for the day: $", Remains)

