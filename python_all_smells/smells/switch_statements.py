def status_message(code):
    if code == "N":
        return "new"
    elif code == "P":
        return "processing"
    elif code == "Q":
        return "quality-check"
    elif code == "S":
        return "shipped"
    elif code == "D":
        return "delivered"
    elif code == "R":
        return "returned"
    return "unknown"
