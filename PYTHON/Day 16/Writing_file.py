# To write data to file, open it in write("w") or append("a") mode.

# 1. Write to a file(overwrite)
file = open("C:/Users/Vani V/OneDrive/Documents/GitHub/text_file.txt", "w")
file.write("Hello, World!")
file.close()

# 2. Append to a file
file = open("C:/Users/Vani V/OneDrive/Documents/GitHub/text_file.txt", "a")
file.write("\nThis is a new line.")
file.close()

# 3. Write multiple lines
file = open("C:/Users/Vani V/OneDrive/Documents/GitHub/text_file.txt", "w")
lines = ("Line 1\n", "Line 2\n", "Line 3\n")
file.writelines(lines)
file.close()