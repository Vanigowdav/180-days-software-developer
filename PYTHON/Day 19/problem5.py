# print characters except vowels
my_str = "aeghifjughwurodkmncv"
vowels = "a", "e", "i", "o", "u"
char = [ char for char in my_str if char not in vowels]
print(char)
          