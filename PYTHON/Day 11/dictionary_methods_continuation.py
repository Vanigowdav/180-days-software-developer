# 4. items() method : return a view object with all the key-value pair in the dictionary including both keys and values.4
    #  synatx : dictionary.items()

pizza = {
    'name' : 'Margheritta Pizza',
    'price' : 8.9,
    'colories_per_slice' : 250,
    'toppings' : ['mozzarella', 'basil']
}
print(pizza.items())

# 5. clear() method: remove all the key-value pair from the dictionary.
    # syntax : dictionary.clear()

print(pizza.clear())


# 6. pop() method : removes the key-value pair with key that you specify as the first argument and return its value.
    #  * if key doesn't exist , it returns the default value that you specify as the second argument.
    # if key doesn't exist and you don't pass a default value, a keyError is raised .
pizza = {
    'name' : 'Margheritta Pizza',
    'price' : 8.9,
    'colories_per_slice' : 250,
    'toppings' : ['mozzarella', 'basil']
}

print(pizza.pop('price', 10))
# print(pizza.pop('total_price'))    # Error raise 

# 7. popitem() method : removes the last inserted item.
pizza = {
    'name' : 'Margheritta Pizza',
    'price' : 8.9,
    'colories_per_slice' : 250,
    'toppings' : ['mozzarella', 'basil']
}
print(pizza.popitem())  

# 8. update()method : updates the key-value pairs with key-values pair of another dictionary.object
pizza = {
    'name' : 'Margheritta Pizza',
    'price' : 8.9,
    'colories_per_slice' : 250,
    'toppings' : ['mozzarella', 'basil']
}
pizza.update({'total_price' : 1000})
print(pizza)