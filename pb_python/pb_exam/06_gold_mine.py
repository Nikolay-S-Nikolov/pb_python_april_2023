location_number = int(input())

for location_count in range(location_number):
    expected_average_gold_per_day = float(input())
    days_per_location = int(input())
    sum_gold = 0
    for days_count in range(days_per_location):
        gold_mined = float(input())
        sum_gold += gold_mined
    average_gold_per_day = sum_gold / days_per_location
    if average_gold_per_day >= expected_average_gold_per_day:
        print(f"Good job! Average gold per day: {average_gold_per_day:.2f}.")
    else:
        print(f"You need {expected_average_gold_per_day - average_gold_per_day:.2f} gold.")
