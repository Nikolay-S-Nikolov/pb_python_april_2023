month = input()
nights = int(input())

studio_price = 0
studio_discount = 0
apartment_price = 0
apartment_discount = 0

if month == "May" or month == "October":
    studio_price = 50.00
    apartment_price = 65.00
    if 7 < nights <= 14:
        studio_discount = 0.05
    elif nights > 14:
        studio_discount = 0.30
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        studio_discount = 0.20
elif month == "July" or month == "August":
    studio_price = 76.00
    apartment_price = 77.00
if nights > 14:
    apartment_discount = 0.10

price_for_apartment = nights * apartment_price * (1 - apartment_discount)
price_for_studio = nights * studio_price * (1 - studio_discount)

print(f"Apartment: {price_for_apartment:.02f} lv.")
print(f"Studio: {price_for_studio:.02f} lv.")
