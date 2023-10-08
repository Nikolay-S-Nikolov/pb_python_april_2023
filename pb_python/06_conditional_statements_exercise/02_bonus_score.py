number=int(input())

bonus_point = 0
if number <= 100:
    bonus_point = 5
elif number <= 1000:
    bonus_point = number * 0.2
else:
    bonus_point = number * 0.1

bonus_extra = 0
if number % 2 == 0:
    bonus_extra = 1
elif number % 10 == 5:
    bonus_extra = 2

total_bonus = bonus_point + bonus_extra
total_number = total_bonus + number

print (total_bonus)
print(total_number)
