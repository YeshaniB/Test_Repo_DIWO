def process_order(items, customer_type):
    total = 0
    count = 0
    subtotal = 0
    tax = 0
    discount = 0
    shipping = 0
    score = 0
    note = ""
    for item in items:
        total += item
        count += 1
    subtotal = total
    if customer_type == "VIP":
        discount = subtotal * 0.15
        score += 10
    else:
        discount = subtotal * 0.05
        score += 2
    after_discount = subtotal - discount
    if after_discount > 500:
        shipping = 0
    else:
        shipping = 25
    taxable = after_discount + shipping
    tax = taxable * 0.18
    final_total = taxable + tax
    if count > 10:
        note += "bulk;"
    if final_total > 1000:
        note += "high-value;"
    if customer_type == "VIP":
        note += "vip;"
    rounded = round(final_total, 2)
    printable = f"items={count}"
    printable += f", subtotal={subtotal}"
    printable += f", discount={discount}"
    printable += f", shipping={shipping}"
    printable += f", tax={tax}"
    printable += f", total={rounded}"
    printable += f", score={score}"
    printable += f", note={note}"
    audit = {"count": count}
    audit["subtotal"] = subtotal
    audit["discount"] = discount
    audit["shipping"] = shipping
    audit["tax"] = tax
    audit["total"] = rounded
    audit["customer_type"] = customer_type
    audit["note"] = note
    if rounded < 0:
        raise ValueError("invalid total")
    return printable, audit
