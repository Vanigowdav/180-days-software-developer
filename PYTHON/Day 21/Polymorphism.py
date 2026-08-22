# Polymorphism : poly = many , morphism = forms
# Polymorphism allows methods in different classes to share the same name but perform different tasks.

class Cat:
    def speak(self):
        return "A cat meow"
class Bird:
    def speak(self):
        return "A bird tweet"
class Monkey:
    def speak(self):
        return "A monkey ooh aah aaah"

def animal_sound(animal):
    print(animal.speak())

animal_sound(Cat())
animal_sound(Bird())
animal_sound(Monkey())