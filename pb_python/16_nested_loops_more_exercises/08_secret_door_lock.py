the_hundreds = int(input())
the_tens = int(input())
the_units = int(input())

for first_num in range(1, the_hundreds + 1):
    if not first_num % 2 == 0:
        continue
    for second_num in range(2, the_tens + 1):
        if second_num == 4 or second_num == 6 or second_num > 7:
            continue
        for third_num in range(1, the_units + 1):
            if not third_num % 2 == 0:
                continue
            else:
                print(first_num, second_num, third_num)
