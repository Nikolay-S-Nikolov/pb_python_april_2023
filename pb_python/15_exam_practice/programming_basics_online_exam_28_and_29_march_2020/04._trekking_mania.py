climbers_groups = int(input())
mussala_count = 0
mont_blanc_count = 0
kilimanjaro = 0
k_2 = 0
everest = 0
total_climbers = 0
for group_n in range(climbers_groups):
    climbers_count = int(input())
    total_climbers += climbers_count
    if climbers_count <= 5:
        mussala_count += climbers_count
    elif climbers_count <= 12:
        mont_blanc_count += climbers_count
    elif climbers_count <= 25:
        kilimanjaro += climbers_count
    elif climbers_count <= 40:
        k_2 += climbers_count
    elif climbers_count >= 41:
        everest += climbers_count

print(f"{mussala_count / total_climbers * 100:.2f}%")
print(f"{mont_blanc_count / total_climbers * 100:.2f}%")
print(f"{kilimanjaro / total_climbers * 100:.2f}%")
print(f"{k_2 / total_climbers * 100:.2f}%")
print(f"{everest / total_climbers * 100:.2f}%")
