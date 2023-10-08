location_number = int(input())

for locations_count in range(location_number):
    expected_average_gold_mining = float(input())
    days_mining_in_location = int(input())
    gold_from_location = 0
    for days_count in range(days_mining_in_location):
        gold = float(input())
        gold_from_location += gold
    average_gold_from_location = gold_from_location/days_mining_in_location
    if average_gold_from_location>= expected_average_gold_mining:
        print(f"Good job! Average gold per day: {average_gold_from_location:.2f}.")
    else:
        print(f"You need {expected_average_gold_mining - average_gold_from_location:.2f} gold.")


