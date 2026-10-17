class Country:
    def __init__(self):
        self.code = "LK"

class Address:
    def __init__(self):
        self.country = Country()

class Profile:
    def __init__(self):
        self.address = Address()

class User:
    def __init__(self):
        self.profile = Profile()

def country_code(user):
    return user.profile.address.country.code
