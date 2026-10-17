from smells.long_method import process_order
from smells.too_many_parameters import create_customer

if __name__ == "__main__":
    print(process_order([10, 20, 30], "VIP"))
    print(create_customer("Ana", "1 Main St", "Colombo", "00100", "0770000000", "a@example.com", "LK"))
