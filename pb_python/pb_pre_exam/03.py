vacation_days = int(input())
room_type = input()  # "room for one person",  "apartment" or "president apartment"
rating = input()  # "positive"  or "negative"

discount = 0
price = 0
if room_type == "room for one person":
    price = 18.00
    discount = 0
elif room_type == "apartment":
    price = 25.00
    if vacation_days <= 10:
        discount = 0.30
    elif vacation_days <= 15:
        discount = 0.35
    elif vacation_days > 15:
        discount = 0.50
elif room_type == "president apartment":
    price = 35.00
    if vacation_days <= 10:
        discount = 0.10
    elif vacation_days <= 15:
        discount = 0.15
    elif vacation_days > 15:
        discount = 0.20

total_price = (vacation_days - 1) * price * (1 - discount)

if rating == "positive":
    total_price += total_price * 0.25
elif rating == "negative":
    total_price -= total_price * 0.10

print(f"{total_price:.2f}")
