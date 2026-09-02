class Logger:
    def log(self, message):
        return f"Log: {message}"
    
class Validator:
    def validate(self, value):
        return value > 0 

class PriceManager(Logger, Validator):
    pass


pm = PriceManager()
print(pm.log("Testing"))
print(pm.validate(50))