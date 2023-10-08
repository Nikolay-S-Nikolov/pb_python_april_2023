budget = float(input())
season = input()  # "summer” или "winter”.
money_spend = 0
destination = ""
accommodation = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        accommodation = "Camp"
        money_spend = budget * 0.30
    elif season == "winter":
        accommodation = "Hotel"
        money_spend = budget * 0.70
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        accommodation = "Camp"
        money_spend = budget * 0.40
    elif season == "winter":
        accommodation = "Hotel"
        money_spend = budget * 0.80
elif budget > 1000:
    destination = "Europe"
    accommodation = "Hotel"
    if season == "summer":
        money_spend = budget * 0.90
    elif season == "winter":
        money_spend = budget * 0.90
print(f"Somewhere in {destination}")
print(f"{accommodation} - {money_spend:.02f}")
