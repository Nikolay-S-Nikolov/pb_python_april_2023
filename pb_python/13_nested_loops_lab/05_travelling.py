destination = input()
money_for_vacation = 0
while not destination == "End":
    needed_budget = float(input())
    saved_money = 0
    while needed_budget > saved_money:
        money_for_vacation = float(input())
        saved_money += money_for_vacation
    print(f"Going to {destination}!")
    destination = input()
