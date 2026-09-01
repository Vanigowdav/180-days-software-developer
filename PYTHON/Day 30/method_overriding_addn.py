class NoteBook:
    name = "Chandras"
    def __init__(self, length, pages, price, notebook_type):
        self.length = length
        self.pages = pages
        self.price = price
        self.type = notebook_type
    def display_info(self):
        return f"{self.name} have a complete range of high quality Student Notebooks especially for schools and colleges."
    def show_details(self):
        return f"The {self.name} is {self.length} notebook , consist of {self.pages} pages, the price of this book is {self.price}, and it is type of {self.type} book only"
    def __str__(self):
        return f"The {self.name} Book has been available in the market for 30 years, The unique style of this book is , it has {self.pages} pages and {self.type} theses varities of books, you can use it for all purpose."
    def updated_price(self, new_price):
        if new_price <=0:
            print("Price cannot be zero")
        else:
            self.price = new_price
class SpiralNoteBook(NoteBook):
    def __init__(self, length, pages, price, notebook_type, spiral_color):
        super().__init__(length, pages, price, notebook_type)
        self.spiral_color = spiral_color
    def spiral_info(self):
        return f"Spiral notebook brand is {self.name} which is {self.spiral_color} color and it has {self.pages} pages."
    def display_info(self):
        parent_msg = super().display_info()
        return f'{parent_msg} It also has a spiral binding for extra durability.'
book = NoteBook("long", 200, 65, "ruled") 
book1 = NoteBook("short", 100, 40, "unruled")
spiralbook = SpiralNoteBook("long", 400, 250, "unruled", "red")
print(spiralbook.show_details())
print(spiralbook.spiral_info())
print(spiralbook.display_info())
print(book.display_info())


