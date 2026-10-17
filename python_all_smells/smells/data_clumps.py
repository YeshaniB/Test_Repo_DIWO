def create_shipping_label(name, address, city, postal_code):
    return f"{name}, {address}, {city}, {postal_code}"

def create_billing_record(name, address, city, postal_code):
    return {"name": name, "address": address, "city": city, "postal_code": postal_code}

def create_delivery_note(name, address, city, postal_code):
    return [name, address, city, postal_code]
