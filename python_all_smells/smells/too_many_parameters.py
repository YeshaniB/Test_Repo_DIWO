def create_customer(name, address, city, postal_code, phone, email, country):
    return {
        "name": name, "address": address, "city": city, "postal_code": postal_code,
        "phone": phone, "email": email, "country": country
    }

def update_customer(name, address, city, postal_code, phone, email, country):
    return f"{name}|{address}|{city}|{postal_code}|{phone}|{email}|{country}"
