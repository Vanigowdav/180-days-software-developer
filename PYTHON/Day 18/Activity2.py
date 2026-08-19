class Mobile:
    def __init__(self, brand, model):
        self.brand  = brand
        self.model = model 
    def display(self):
        print(f'The mobile is  a {self.brand} {self.model} ')

Brand1 = Mobile("Samsaung Galaxy", "S21")  
Brand2 = Mobile("Vivo", "Y21")

Brand1.display()
Brand2.display()