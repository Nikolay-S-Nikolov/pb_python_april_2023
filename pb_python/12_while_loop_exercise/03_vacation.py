excursion_money = float(input())
current_money = float(input())
spend_money_days = 0
days_counter = 0

while current_money < excursion_money:
    command = input()
    money = float(input())
    days_counter += 1
    if command == "save":
        current_money += money
        spend_money_days = 0
    elif command == "spend":
        current_money -= money
        spend_money_days += 1
        if spend_money_days == 5:
            print(f"You can't save the money.")
            print(days_counter)
            break
        if current_money <= 0:
            current_money = 0
if current_money >= excursion_money:
    print(f"You saved the money for {days_counter} days.")
