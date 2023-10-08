groups_count = int(input())
musalla_group = 0
mont_blanc_group = 0
kilimanjaro_group = 0
k2_group = 0
everest_group = 0
total_climbers = 0
for _ in range(groups_count):
    climbers_count = int(input())
    total_climbers += climbers_count
    if climbers_count < 6:
        musalla_group += climbers_count
    elif climbers_count < 13:
        mont_blanc_group += climbers_count
    elif climbers_count < 26:
        kilimanjaro_group += climbers_count
    elif climbers_count < 41:
        k2_group += climbers_count
    elif climbers_count >= 41:
        everest_group += climbers_count
musalla_percentage = musalla_group / total_climbers * 100
mont_blanc_percentage = mont_blanc_group / total_climbers * 100
kilimanjaro_percentage = kilimanjaro_group / total_climbers * 100
k2_percentage = k2_group / total_climbers * 100
everest_percentage = everest_group / total_climbers * 100

print(f"{musalla_percentage:.2f}%")
print(f"{mont_blanc_percentage:.2f}%")
print(f"{kilimanjaro_percentage:.2f}%")
print(f"{k2_percentage:.2f}%")
print(f"{everest_percentage:.2f}%")