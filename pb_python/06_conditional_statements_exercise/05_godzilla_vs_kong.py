movie_budget = float(input())
extra_actor = int(input())
clothes_price_extra_actor = float(input())

decor_price = movie_budget * 0.10

discount_clothes = 0
if extra_actor > 150:
    discount_clothes = 0.10

clothes_price = extra_actor * clothes_price_extra_actor * (1 - discount_clothes)

total_movie_price = decor_price + clothes_price

money_left = movie_budget - total_movie_price

if total_movie_price > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs { - money_left:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
