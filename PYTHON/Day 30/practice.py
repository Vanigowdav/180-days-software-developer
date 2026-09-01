# Notebook 
class NoteBook:
    name = "Chandras"
    def __init__(self, length, pages, price, notebook_type):
        self.length = length
        self.pages = pages
        self.price = price
        self.type = notebook_type
    def display_into(self):
        return f"{self.name} have a complete range of high quality Student Notebooks especially for schools and colleges."
    def show_details(self):
        return f"The {self.name} is {self.length} notebook , consist of {self.pages} pages, the price of this book is {self.price}, and it is type of {self.type} book only"

book = NoteBook("long", 200, 65, "ruled") 
book1 = NoteBook("short", 100, 40, "unruled")
book.name = "Akshara"
print(book.display_into()) 
print(book.show_details())
print(book1.show_details())
print(book1.name)
print(book.name)  