#Operators: Operators are special symbols that carry out arithmetic or logical computation. 
# The value that the operator operates on is called the operand.

# symobls : +, -, *, /, % (Modulus), **(power), // (floor division), =, ==, !=(not equal), >, <, >=, <=
#------Students marks calculation------
subject1 = int(input("Enter the marks of subject1:"))   
subject2 = int(input("Enter the marks of subject2:"))
subject3 = int(input("Enter the marks of subject3:"))
subject4 = int(input("Enter the marks of subject4:"))
total_marks = subject1 + subject2 + subject3 + subject4
average_marks = total_marks / 4
percentage = total_marks / 400 * 100
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Percentage:", percentage,"%")


#Floor Division: Floor division is a mathematical operation that divides one number by another and 
# returns the largest integer less than or equal to the result.
floor_division_result = 10 // 3
print("Floor Division Result:", floor_division_result)

#Modulus: Modulus is a mathematical operation that returns the remainder of a division operation.
modulus_result = 10 % 3
print("Modulus Result:", modulus_result)

#power: Power is a mathematical operation that raises a number to a certain exponent.
power_result = 2 ** 3
print("Power Result:", power_result)

#not equal: Not equal is a comparison operator that checks if two values are not equal to each other.
not_equal_result = 10 != 5
print("Not Equal Result:", not_equal_result)

