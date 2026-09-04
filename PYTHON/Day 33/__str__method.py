from http import client


class Feedback:
    def __init__(self, name, rating, comment):
        self.name = name 
        self.rating = rating
        self.comment = comment
    def __str__(self):
        return f"{self.name} rated {self.rating}/5 {self.comment}!."


client1 = Feedback("nisha", 4, "Greet Service")
print(client1)     # Python automatically call str method                       

# Using __str_ method :
 # This method is automatically called when we do print(object)
        # Without this method, print(feedback) would show something like:
        # <__main__.Feedback object at 0x000001DB3AE906E0>
        # With this method, we control exactly what string gets printed