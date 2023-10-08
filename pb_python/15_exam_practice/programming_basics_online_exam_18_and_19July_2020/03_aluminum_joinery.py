windows_count = int(input())
windows_type = input()  # can be "90X130" or "100X150" or "130X180" or "200X300";
delivery_type = input()  # "With delivery" or "Without delivery"
unit_price = 0
price = 0

if windows_count < 10:
    print("Invalid order")
else:
    if windows_type == "90X130":
        unit_price = 110
        if windows_count > 60:
            unit_price -= 110 * 0.08
        elif windows_count > 30:
            unit_price -= 110 * 0.05
    elif windows_type == "100X150":
        unit_price = 140
        if windows_count > 80:
            unit_price -= 140 * 0.10
        elif windows_count > 40:
            unit_price -= 140 * 0.06
    elif windows_type == "130X180":
        unit_price = 190
        if windows_count > 50:
            unit_price -= 190 * 0.12
        elif windows_count > 20:
            unit_price -= 190 * 0.07
    elif windows_type == "200X300":
        unit_price = 250
        if windows_count > 50:
            unit_price -= 250 * 0.14
        elif windows_count > 25:
            unit_price -= 250 * 0.09
    price = windows_count * unit_price
    if delivery_type == "With delivery":
        price += 60
    if windows_count > 99:
        price = price * 0.96

    total_to_pay = price
    print(f"{total_to_pay:.2f} BGN")
