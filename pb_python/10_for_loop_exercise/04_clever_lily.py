age = int(input())
laundry_machine_price = float(input())
toy_price = int(input())
collected_money = 0
for age_count in range(1, age + 1):
    if age_count % 2 == 0:
        collected_money += age_count * 5 - 1
    else:
        collected_money += toy_price
if collected_money >= laundry_machine_price:
    print(f"Yes! {collected_money - laundry_machine_price:.02f}")
else:
    print(f"No! {laundry_machine_price - collected_money:.02f}")
