# number_n = int(input())
#
# for first_special in range(1, 10):
#     if not number_n % first_special == 0:
#         continue
#     for second_special in range(1, 10):
#         if not number_n % second_special == 0:
#             continue
#         for third_special in range(1, 10):
#             if not number_n % third_special == 0:
#                 continue
#             for fourth_special in range(1, 10):
#                 if not number_n % fourth_special == 0:
#                     continue
#                 else:
#                     print(f"{first_special}{second_special}{third_special}{fourth_special}", end=' ')

number_n = int(input())

for number in range(1_111, 10_000):
    special_num = str(number)
    is_special = True

    for _, special_number in enumerate(special_num):
        special_number = int(special_number)

        if special_number == 0:
            is_special = False
            break

        if not number_n % special_number == 0:
            is_special = False
            break

    if is_special:
        print(f"{number}", end=' ')
