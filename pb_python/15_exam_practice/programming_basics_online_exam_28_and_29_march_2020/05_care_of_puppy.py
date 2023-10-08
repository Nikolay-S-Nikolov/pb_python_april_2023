food_bought_kg = int(input())
available_food_gr = food_bought_kg * 1000
command = input()
eaten_food = 0
while not command == "Adopted":
    today_food = int(command)
    eaten_food += today_food
    command = input()
if available_food_gr >= eaten_food:
    print(f"Food is enough! Leftovers: {available_food_gr-eaten_food} grams.")
else:
    print(f"Food is not enough. You need {eaten_food-available_food_gr} grams more.")
