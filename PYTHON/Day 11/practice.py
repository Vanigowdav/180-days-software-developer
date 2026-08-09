people = {
    'Vani' : 20,
    'Ananya' : 23,
    'Nayan' : 24
}
def greeting(name, age):
    print(f'Hello {name}!, You are {age} years old')

for name, age in people.items():
    greeting(name, age)
    