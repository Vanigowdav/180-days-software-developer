# Notification System 
class Notification:
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message
    def send(self):
        return f"Sending notification"
    def __str__(self):
        return f"Sending notification to {self.recipient} : '{self.message}'"
    def __eq__(self, other):
        return self.recipient == other.recipient and self.message == other.message

class Emailnotification(Notification):
    def __init__(self, recipient, message, email):
        super().__init__(recipient, message)
        self.email = email
    def send(self):
        return f" Email sent to {self.email}"
class SMSNotification(Notification):
    def __init__(self, recipient, message, phone_number):
        super().__init__(recipient, message)
        self.phone_number = phone_number
    def send(self):
        return f"SMS sent to {self.phone_number}"

mail = Emailnotification("eagle", "Hi Bro!","eagle@email.com")
user = SMSNotification("eagle", "Hi Bro!", 5463215690)
mail1 = Emailnotification("nanu", "Hi Bro!", "eagle@email.com")
# print(mail)
# print(user)
print(mail == mail1)
# print(mail.send())
# print(user.send())
        