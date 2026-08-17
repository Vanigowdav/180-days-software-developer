# Once a file is opened in read mode, you can read its content.

# 1. Read the entire file :
file = open("C:/Users/Vani V/OneDrive/Documents/GitHub/text_file.txt", "r")
content = file.read()
print(content)
file.close()

# 2. Read line by line 
file = open("C:/Users/Vani V/OneDrive/Documents/GitHub/text_file.txt", "r")
for line in file:
    print(line)
file.close()

# 3. Read specific number of characters
file = open("C:/Users/Vani V/OneDrive/Documents/GitHub/text_file.txt", "r")
content = file.read(10)
print(content)
file.close()
