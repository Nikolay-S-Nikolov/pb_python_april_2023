days_reservation = int(input())
type_room = input()
rating = input()

price_per_night = 0
discount = 0
if type_room == "room for one person":
    price_per_night = 18.00
elif type_room == "apartment":
    price_per_night = 25.00
    if days_reservation < 10:
        discount = 0.30
    elif days_reservation < 15:
        discount = 0.35
    elif days_reservation >= 15:
        discount = 0.50
elif type_room == "president apartment":
    price_per_night = 35.00
    if days_reservation < 10:
        discount = 0.10
    elif days_reservation < 15:
        discount = 0.15
    elif days_reservation >= 15:
        discount = 0.20

price_for_vacation = (days_reservation - 1) * price_per_night * (1 - discount)
rating_discount = 0
if rating == "positive":
    rating_discount = -0.25
elif rating == "negative":
    rating_discount = 0.10
final_price = price_for_vacation * (1 - rating_discount)
print(f"{final_price:.02f}")
