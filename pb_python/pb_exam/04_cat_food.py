cat_count = int(input())

group_1_count = 0
group_2_count = 0
group_3_count = 0
eaten_food = 0
for cat_num in range(1, cat_count + 1):
    cat_food_grams = float(input())
    eaten_food += cat_food_grams
    if 100 <= cat_food_grams < 200:
        group_1_count += 1
    elif cat_food_grams < 300:
        group_2_count += 1
    elif cat_food_grams < 400:
        group_3_count += 1
price_for_food = eaten_food / 1000 * 12.45
print(f"Group 1: {group_1_count} cats.")
print(f"Group 2: {group_2_count} cats.")
print(f"Group 3: {group_3_count} cats.")
print(f"Price for food per day: {price_for_food:.2f} lv.")
