CALORIES_PER_MINUTE = 5

minutes_per_tour = int(input())
number_tours_per_day = int(input())
calories_intake = int(input())

total_burned_calories = number_tours_per_day * minutes_per_tour * CALORIES_PER_MINUTE

if (calories_intake/2) <= total_burned_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_burned_calories}.")
