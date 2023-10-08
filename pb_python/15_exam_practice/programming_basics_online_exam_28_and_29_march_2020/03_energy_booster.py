fruit = input()  # Watermelon", "Mango", "Pineapple" или "Raspberry"
size = input()  # "small" или "big"
count_ordered = int(input())
price = 0

if fruit == "Watermelon":
    if size == 'small':
        price = 2 * 56.00
    elif size == "big":
        price = 5 * 28.70
elif fruit == "Mango":
    if size == 'small':
        price = 2 * 36.66
    elif size == "big":
        price = 5 * 19.60
elif fruit == "Pineapple":
    if size == 'small':
        price = 2 * 42.10
    elif size == "big":
        price = 5 * 24.80
elif fruit == "Raspberry":
    if size == 'small':
        price = 2 * 20.00
    elif size == "big":
        price = 5 * 15.20
total_price = count_ordered * price
if total_price > 1000:
    total_price -= total_price * 0.50
elif total_price >= 400:
    total_price -= total_price * 0.15

print(f"{total_price:.2f} lv.")
