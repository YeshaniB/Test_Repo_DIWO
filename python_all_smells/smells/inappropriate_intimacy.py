class BankAccount:
    def __init__(self):
        self._balance = 1000
        self._pin = "1234"

class Auditor:
    def inspect(self, account):
        return account._balance, account._pin
