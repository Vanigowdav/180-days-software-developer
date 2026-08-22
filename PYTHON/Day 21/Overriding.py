# Overriding : means the child class rewrites a method that already exist in parent class.


class Parents:
    def work(self):
        print("Works 9 to 5")
class Child(Parents):
    def work(self):
        print("Work as freelancer from home")

p = Parents()
p.work()

c = Child()
c.work()


# Overide the sound() method from the parent Animal class in the child Dog class so we can have sound() use the bark class variable.
class Animal:
    def __init__(self, name):
        self.name = name 
    def sound(self):
        return f'{self.name} makes a sound'
class Dog(Animal):
    bark = "woof! woof!! woof!!!"
    def sound(self):
        return f'{self.name} barks {self.bark}'

jack = Dog('Jack')
print(jack.sound())
print(jack.bark)