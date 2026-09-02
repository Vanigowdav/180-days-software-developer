# class Printable:
#     def info(self):
#         return f"This notebook can be printed for reference"

# class Sellable:
#     def sell(self):
#         return f"This notebook is avaible for sale"


# class NoteBook(Printable, Sellable):
#     pass

# nb = NoteBook()
# print(nb.info())
# print(nb.sell())

class Printable:
    def info(self):
        return f"This notebook can be printed for reference"
    def describe(self):
        return f"Printable version"
class Sellable:
    def sell(self):
        return f"This notebook is avaible for sale"
    def describe(self):
        return f"Sellable version"

class NoteBook(Printable, Sellable):
    pass

nb = NoteBook()
print(nb.describe())
print(nb.describe())