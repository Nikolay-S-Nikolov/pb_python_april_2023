cargo_capacity = float(input())
command = input()
loaded_luggage_count = 0
no_more_space = False
while not command == "End":
    suitcase_volume = float(command)
    cargo_capacity -= suitcase_volume
    if (loaded_luggage_count+1) % 3 == 0:
        cargo_capacity -= suitcase_volume * 0.10
    if cargo_capacity <= 0:
        no_more_space = True
        break
    else:
        loaded_luggage_count += 1
    command = input()

if no_more_space:
    print("No more space!")
    print(f"Statistic: {loaded_luggage_count} suitcases loaded.")
else:
    print("Congratulations! All suitcases are loaded!")
    print(f"Statistic: {loaded_luggage_count} suitcases loaded.")
