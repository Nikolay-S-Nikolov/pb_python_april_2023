coins_1lv_count = int(input())
coins_2lv_count = int(input())
notes_5lv_count = int(input())
amount = int(input())

for num_1lv in range(coins_1lv_count + 1):
    for num_2lv in range(coins_2lv_count + 1):
        for num_5lv in range(notes_5lv_count + 1):
            if num_1lv + num_2lv * 2 + num_5lv * 5 == amount:
                print(f"{num_1lv} * 1 lv. + {num_2lv} * 2 lv. + {num_5lv} * 5 lv. = {amount} lv.")
