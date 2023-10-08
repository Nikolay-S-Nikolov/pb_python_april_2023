pocket_money_per_day = float(input())
earned_per_day_from_sales = float(input())
expenses_for_entire_period = float(input())
gift_price = float(input())

saved_money = 5 * pocket_money_per_day + 5 * earned_per_day_from_sales
all_saved_money = saved_money - expenses_for_entire_period

if all_saved_money >= gift_price:
    print(f"Profit: {all_saved_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {gift_price - all_saved_money:.2f} BGN.")
