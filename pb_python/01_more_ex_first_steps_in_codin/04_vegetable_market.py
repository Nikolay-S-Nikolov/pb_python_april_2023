vegetables_price_kg = float(input())
fruit_price_kg = float(input())
total_vegetables_weight = int(input())
total_fruit_weight = int(input())

vegetables_income = vegetables_price_kg * total_vegetables_weight
fruit_income = fruit_price_kg * total_fruit_weight
total_income_euro = (vegetables_income + fruit_income) / 1.94
print(f"{total_income_euro:.02f}")
