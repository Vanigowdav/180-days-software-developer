# # 1. Opening a file for reading
file = open("C:/Users/Vani V/OneDrive/Documents/GitHub/text_file.txt", "r")
print(file.name)
print(file.mode)
file.close()

# 2. Opening a file for writing
file = open("C:/Users/Vani V/OneDrive/Documents/GitHub/text_file.txt", "w")
file.close()

# # 3. Opening a file for appending
# file = open("text_file.txt", "a")
