def calculate_invoice(amount):
    service_fee = amount * 0.075
    late_fee = 47
    risk_limit = 913
    if amount > risk_limit:
        late_fee += 23
    return amount + service_fee + late_fee
