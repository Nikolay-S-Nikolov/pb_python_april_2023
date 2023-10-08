num_n = int(input())
num_l = int(input())

for first_number in range(1, num_n):
    for second_number in range(1, num_n):
        range_last_number = 2
        if first_number >= second_number:
            range_last_number = first_number + 1
        else:
            range_last_number = second_number + 1
        for firs_letter in range(97, 97 + num_l):
            for second_letter in range(97, 97 + num_l):
                for last_number in range(range_last_number, num_n + 1):
                    print(f"{first_number}{second_number}{chr(firs_letter)}{chr(second_letter)}{last_number}", end=" ")
