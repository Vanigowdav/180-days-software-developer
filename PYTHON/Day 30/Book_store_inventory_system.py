class NoteBook:
    def __init__(self, name, length, pages, price, notebook_type):
        self.name = name
        self.length = length
        self.pages = pages
        self.price = price
        self.type = notebook_type
    def __str__(self):
            return f"{self.name}"
    

class Bookstore():
    def __init__(self):
        self.store = []
    def add_book(self, new_book):
        self.store.append(new_book)
    def total_value(self):
        total_price = 0
        for book in self.store:
            total_price += book.price
        return total_price
    def show_all(self):
        for book in self.store:
            print(book)

b1 = NoteBook("chandras","long", 300, 130, "ruled")
b2 = NoteBook("akshara","short", 100, 60, "unruled")
mystore = Bookstore()
mystore.add_book(b1)
mystore.add_book(b2)
print(mystore.total_value())
mystore.show_all()
