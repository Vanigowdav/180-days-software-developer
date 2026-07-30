#String slicing : Extract portion of a string or work with only a specific part of it 
#Syntax = [start index : stop index]  : it includes start index value but excludes last index value 
my_str = "My fav car is RangeRover"
print(my_str[0:9])                    #0:8 it print the output 

#Omiting start and stop index 
# 1. Omit start index : extract everything from index 0 upto stop index
my_str = "My fav car is RangeRover"
print(my_str[:9])   

# 2. Omit stop index : extract everything from index start upto end
my_str = "My fav car is RangeRover"
print(my_str[3:])  

# 3. Omit both  indexes : 
my_str = "My fav car is RangeRover"
print(my_str[:])   


#Remember slicing string does not modify or alter the string , the original string will be as it is 
print(my_str)

#Another index called step : used to specify the increment between each index in slice 
#Syntax : [start:stop:step]
my_str = "My fav car is RangeRover"
print(my_str[0:24:2]) 

#Important : Reverse a string using step index by setting step to -1 and leaving start and stop index blank 
print(my_str[::-1])


