from math import ceil

name = input()
initial_budget = float(input())
beer_bottle_pieces = int(input())
chips_packs_number = int(input())

all_beers_price = 1.20 * beer_bottle_pieces
chips_price = all_beers_price * (1 - 0.55) * chips_packs_number
chips_price = ceil(chips_price)
total_amount_to_pay = all_beers_price + chips_price
if total_amount_to_pay <= initial_budget:
    print(f"{name} bought a snack and has {initial_budget - total_amount_to_pay:.2f} leva left.")
else:
    print(f"{name} needs {total_amount_to_pay - initial_budget:.2f} more leva!")
