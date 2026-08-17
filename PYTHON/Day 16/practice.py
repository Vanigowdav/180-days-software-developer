# Calculate the sum of numbers in a file

file = open("C:/Users/Vani V/OneDrive/Documents/GitHub/data.txt", "r")
total = 0
for line in file:
    total += int(line.strip())
file.close()
print("The sum of the number is:", total)