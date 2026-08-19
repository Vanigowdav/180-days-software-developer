class Student:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks
    def display_method(self):
        print(f'{self.name} scored {self.marks}  out of 25 in First Assessment')
student1 = Student("Thilak", 23)
student2 = Student("Chandan", 24)
student3 = Student("Rishi", 25)

student1.display_method()
student2.display_method()
student3.display_method()