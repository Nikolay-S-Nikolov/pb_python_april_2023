excursions_sea_count = int(input())
excursions_mountain_count = int(input())
command = input()

profit = 0
while not command == "Stop":
    if command == "sea" and not excursions_sea_count == 0:
        profit += 680
        excursions_sea_count -= 1
    elif command == "mountain" and not excursions_mountain_count == 0:
        profit += 499
        excursions_mountain_count -= 1
    if excursions_sea_count == 0 and excursions_mountain_count == 0:
        break
    command = input()
if excursions_sea_count == 0 and excursions_mountain_count == 0:
    print(" Good job! Everything is sold.")

print(f"Profit: {profit} leva.")
