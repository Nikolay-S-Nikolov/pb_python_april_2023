upper_limit_first_number = int(input())
upper_limit_second_number = int(input())
upper_limit_third_number = int(input())
for first_number in range(1, upper_limit_first_number + 1):
    if not first_number % 2 == 0:
        continue
    for second_number in range(2, upper_limit_second_number + 1):
        if second_number > 7 or second_number == 4 or second_number == 6 :
            continue
        for third_number in range(1, upper_limit_third_number + 1):
            if not third_number % 2 == 0:
                continue
            else:
                print(f"{first_number} {second_number} {third_number}")

