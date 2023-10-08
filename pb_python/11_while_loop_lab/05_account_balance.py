account_balance = input()
total_sum = 0
while account_balance != "NoMoreMoney":
    current_sum = float(account_balance)
    if current_sum < 0:
        print("Invalid operation!")

        break
    total_sum += current_sum
    print(f"Increase: {current_sum:.2f}")
    account_balance = input()
print(f"Total: {total_sum:.2f}")