class Customer:
    def __init__(self):
        self.name = "Nimal"
        self.email = "nimal@example.com"
        self.phone = "0770000000"
        self.city = "Colombo"
        self.country = "Sri Lanka"
        self.account_status = "ACTIVE"

class CustomerReporter:
    def describe(self, customer):
        return (
            customer.name + "|" + customer.email + "|" + customer.phone + "|" +
            customer.city + "|" + customer.country + "|" + customer.account_status
        )
