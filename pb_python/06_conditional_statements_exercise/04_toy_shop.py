PUZZEL_PRICE = 2.60
TALKING_DOLL = 3.00
TEDY_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2.00

price_excursion = float(input())
puz_numbers = int(input())
talking_doll_numbers = int(input())
tedy_numbers = int(input())
minion_number = int(input())
truck_numbers = int(input())

total_toys = puz_numbers + talking_doll_numbers + tedy_numbers + minion_number + truck_numbers

discount = 0
if total_toys >= 50:
    discount = 0.25

total_price = PUZZEL_PRICE * puz_numbers + TALKING_DOLL * talking_doll_numbers +\
              TEDY_PRICE * tedy_numbers + MINION_PRICE * minion_number + TRUCK_PRICE * truck_numbers

price_with_discount = total_price - total_price * discount
total_amount = price_with_discount - price_with_discount * 0.10

price_total_minus_excursion_amount = total_amount -  price_excursion

if total_amount >= price_excursion:
    print(f"Yes! {price_total_minus_excursion_amount:.2f} lv left.")
else:
    print(f"Not enough money! {- price_total_minus_excursion_amount:.2f} lv needed.")
