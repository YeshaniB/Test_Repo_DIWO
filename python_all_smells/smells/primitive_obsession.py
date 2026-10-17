class CustomerRecord:
    name: str
    age: int
    balance: float
    active: bool
    city: str

    def __init__(self, name: str, age: int, balance: float, active: bool, city: str):
        self.name = name
        self.age = age
        self.balance = balance
        self.active = active
        self.city = city
