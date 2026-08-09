# 1. get() method : used to retrieve the value associated with a key.
    #  syntax : dictionary.get(key, default)    if you mention default value we won't get error if key is not found.

pizza = {
    'name' : 'Margheritta Pizza',
    'price' : 8.9,
    'colories_per_slice' : 250,
    'toppings' : ['mozzarella', 'basil']
}
print(pizza)
print(pizza.get('name',[]))

# 2. key() method: return a view object will all the keys. [view object is just a way to see the content of a dictionary without creating a separate copy of the data.]
    #  syntax : dictionary.key()


pizza = {
    'name' : 'Margheritta Pizza',
    'price' : 8.9,
    'colories_per_slice' : 250,
    'toppings' : ['mozzarella', 'basil']
}
print(pizza.keys())


# 2. values() method: return all the values.
    #  syntax : dictionary.values()


pizza = {
    'name' : 'Margheritta Pizza',
    'price' : 8.9,
    'colories_per_slice' : 250,
    'toppings' : ['mozzarella', 'basil']
}
print(pizza.values())