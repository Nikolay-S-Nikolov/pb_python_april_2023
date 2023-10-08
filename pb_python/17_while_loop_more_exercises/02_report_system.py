expected_amount = int(input())
command = input()

counter = 0
cash_counter = 0
cash_amount = 0
card_counter = 0
card_amount = 0
while not command == "End":
    transaction = int(command)
    counter += 1
    if not counter % 2 == 0:
        if transaction > 100:
            print("Error in transaction!")
        else:
            expected_amount -= transaction
            cash_amount += transaction
            print("Product sold!")
    else:
        if transaction < 10:
            print("Error in transaction!")
        else:
            expected_amount -= transaction
            card_amount += transaction
            print("Product sold!")
    if expected_amount <= 0:
        break
    command = input()

if expected_amount <= 0:
    print(f"Average CS: {cash_amount / cash_counter:.2f}")
    print(f"Average CC: {card_amount / card_counter:.2f}")
else:
    print("Failed to collect required money for charity.")
