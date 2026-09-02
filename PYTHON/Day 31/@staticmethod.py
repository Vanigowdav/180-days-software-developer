class NoteBook:
    def __init__(self, name, length, pages, price, notebook_type):
        self.name = name
        self.length = length
        self.pages = pages
        self._price = price
        self.type = notebook_type
    @staticmethod
    def is_valid_price(price):
        return price > 0

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if self.is_valid_price(new_price):
             self._price = new_price
        else:
            print("invalid")


b1 = NoteBook("chandras","long", 300, 130, "ruled")

b1.price = 200
print(b1.is_valid_price(b1.price))
print(b1.price)

# ಗಮನಿಸಿ:

# @staticmethod decorator ಬಳಸಿದ್ದೀವಿ
# Method ಗೆ self ಇಲ್ಲ! ಬರೀ price ಅನ್ನೋ parameter ಮಾತ್ರ
# ಇದನ್ನ call ಮಾಡೋಕೆ: NoteBook.is_valid_price(50) (class ಹೆಸರು ಬಳಸಿ, object ಬೇಕಾಗಿಲ್ಲ!) ಅಥವಾ book.is_valid_price(50) (object ಇಂದ ಕೂಡ call ಮಾಡ್ಬಹುದು)