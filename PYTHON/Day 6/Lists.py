# Lists is a datatype in Python that is used to store multiple items in a single variable. 
# List are ordered, changeable, and allow duplicate values. 
# List are defined by enclosing the items in square brackets[].

film_stars = ["Darshan", "Sudeep", "Yash", "Puneeth", "Girish"]
print(film_stars) 

#To access the elements of a list, we can use the index number of the element.
print(film_stars[0]) # Output: Darshan
print(film_stars[1]) # Output: Sudeep

#To access last element of a list, we can use negative index number.
print(film_stars[-1]) # Output: Girish

#To change the value of a specific item in a list, we can use the index number of the item.
film_stars[0] = "Ravi"
print(film_stars) # Output: ['Ravi', 'Sudeep', 'Yash', 'Puneeth', 'Girish']

# Another way to create a list is to use the list() constructor.
developer = "Vani"
print(list(developer)) # Output: ['V', 'a', 'n', 'i']

#To get total number of items in a list, we can use the len() function.
number_of_stars = len(film_stars)
print(f"Total number of film stars: {number_of_stars}") # Output: Total number of film stars: 5



