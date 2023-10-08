first_num_begin = int(input())
second_num_begin = int(input())
first_num_end = int(input())
second_num_end = int(input())

for first_couple in range(first_num_begin, first_num_begin + first_num_end + 1):
    first_couple_is_prime_number = True
    for first_couple_prime_number_check in range(2, first_couple):
        if first_couple % first_couple_prime_number_check == 0:
            first_couple_is_prime_number = False
    if not first_couple_is_prime_number:
        continue
    for second_couple in range(second_num_begin, second_num_begin + second_num_end + 1):
        second_couple_is_prime_number = True
        for second_couple_prime_number_check in range(2, second_couple):
            if second_couple % second_couple_prime_number_check == 0:
                second_couple_is_prime_number = False
        if not second_couple_is_prime_number:
            continue
        print(f"{first_couple}{second_couple}")
