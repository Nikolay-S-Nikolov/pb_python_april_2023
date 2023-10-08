extra_20_kg_luggage_price = float(input())
luggage_kg = float(input())
days_left = int(input())
luggage_count = int(input())

extra_luggage_price = 0
if luggage_kg < 10:
    extra_luggage_price = extra_20_kg_luggage_price * 0.20
elif luggage_kg <= 20:
    extra_luggage_price = extra_20_kg_luggage_price * 0.50
elif luggage_kg > 20:
    extra_luggage_price = extra_20_kg_luggage_price
if days_left > 30:
    extra_luggage_price += extra_luggage_price * 0.10
elif days_left >= 7:
    extra_luggage_price += extra_luggage_price * 0.15
elif days_left < 7:
    extra_luggage_price += extra_luggage_price * 0.40

price_to_pay = extra_luggage_price * luggage_count
print(f"The total price of bags is: {price_to_pay:.2f} lv.")
