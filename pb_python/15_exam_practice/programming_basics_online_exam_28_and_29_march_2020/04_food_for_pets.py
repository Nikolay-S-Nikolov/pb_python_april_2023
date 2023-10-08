days_count = int(input())
total_food_amount = float(input())
dog_food = 0
cat_food = 0
total_eaten_biscuits = 0
for days in range(1, days_count + 1):
    today_dog_food = int(input())
    dog_food += today_dog_food
    today_cat_food = int(input())
    cat_food += today_cat_food
    if days % 3 == 0:
        biscuits_reword = (today_cat_food + today_dog_food) * 0.10
        total_eaten_biscuits += biscuits_reword

eaten_food_percentage = (cat_food + dog_food) / total_food_amount * 100
dog_food_percentage = dog_food / (cat_food + dog_food) * 100
cat_food_percentage = cat_food / (cat_food + dog_food) * 100
print(f"Total eaten biscuits: {total_eaten_biscuits:.0f}gr.")
print(f"{eaten_food_percentage:.2f}% of the food has been eaten.")
print(f"{dog_food_percentage:.2f}% eaten from the dog.")
print(f"{cat_food_percentage:.2f}% eaten from the cat.")
