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
    def __str__(self):
        return f"The {self.name} Book has been available in the market for 30 years, The unique style of this book is , it has {self.pages} pages and {self.type} theses varities of books, you can use it for all purpose."
    def updated_price(self, new_price):
        if new_price <=0:
            print("Price cannot be zero")
        else:
            self.price = new_price
book = NoteBook("long", 200, 65, "ruled") 
book1 = NoteBook("short", 100, 40, "unruled")
book.name = "Akshara"

book.updated_price(-5)
print(book.price)
book.updated_price(100)
print(book.price)


#Added new feature ie., updated price of book by update method insted of using eg.book.price = 380