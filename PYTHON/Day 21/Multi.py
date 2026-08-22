class Walker:
    def walk(self):
        return f'I can walk on land'
class Swimmer:
    def swim(self):
        return 'I can swim in water'

class Amphibian(Walker, Swimmer):
    def __init__(self, name):
        self.name = name 
    def introduce(self):
        return f"I am {self.name} the frog. {self.walk()} and {self.swim()}"

frog = Amphibian('Freedy')
print(frog.introduce())
        