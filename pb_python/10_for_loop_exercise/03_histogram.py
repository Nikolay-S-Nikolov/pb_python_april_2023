number_n = int(input())

number_p1 = 0
number_p2 = 0
number_p3 = 0
number_p4 = 0
number_p5 = 0

for _ in range(1, number_n + 1):
    new_number = int(input())
    if new_number < 200:
        number_p1 += 1
    elif new_number < 400:
        number_p2 += 1
    elif new_number < 600:
        number_p3 += 1
    elif new_number < 800:
        number_p4 += 1
    elif new_number > 799:
        number_p5 += 1
percentage_p1 = 100 * number_p1 / number_n
percentage_p2 = 100 * number_p2 / number_n
percentage_p3 = 100 * number_p3 / number_n
percentage_p4 = 100 * number_p4 / number_n
percentage_p5 = 100 * number_p5 / number_n
print(f"{percentage_p1:.02f}%")
print(f"{percentage_p2:.02f}%")
print(f"{percentage_p3:.02f}%")
print(f"{percentage_p4:.02f}%")
print(f"{percentage_p5:.02f}%")