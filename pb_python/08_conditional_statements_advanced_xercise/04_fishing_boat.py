budget = int(input())
season = input()  # "Spring", "Summer", "Autumn" или "Winter";
fisherman_number = int(input())

price_rent = 0
discount = 0
extra_discount = 0
if season == "Spring":
    price_rent = 3000
elif season == "Summer" or season == "Autumn":
    price_rent = 4200
elif season == "Winter":
    price_rent = 2600

if fisherman_number <= 6:
    discount = 0.10
elif fisherman_number <= 11:
    discount = 0.15
elif fisherman_number > 11:
    discount = 0.25
if fisherman_number % 2 == 0 and not season == "Autumn":
    extra_discount = 0.05

fishing_cost = price_rent * (1 - discount) * (1 - extra_discount)
if budget >= fishing_cost:
    print(f"Yes! You have {budget - fishing_cost:.02f} leva left.")
else:
    print(f"Not enough money! You need {fishing_cost - budget:.02f} leva.")
