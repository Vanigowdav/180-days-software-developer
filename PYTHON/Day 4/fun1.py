# 1. square of numbers:

def squ_num(num):
    return num **2

result = squ_num(3)
print(result)


#---- or
def squ_num(num):
    return num * num

result = squ_num(3)
print(result) 



# 2. cube function
def cube_num(num):
    return num ** 3

print(cube_num(3))


#major diffference to see when we use return  or not
def add_num(a, b):
    print(a + b)


def add_num_return(a, b):
    return a + b


x = add_num(2, 3)                                        # here x values gives none bcz fun not return anything back
y = add_num_return(2, 3)
print(x)
print(y)