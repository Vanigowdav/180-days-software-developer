# Consider a User class for storing login information.

class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password  #Private attribute

    def get_username(self):
        return self.username

    def check_password(self, password):
        return password == self._password


user = User("dev_gowda", "pass124")
print(user.get_username()) #Access allowed
print(user.check_password("wrong_pass"))     # Return False
print(user.check_password("pass1234"))       # Return True