# # letter = input()
# # letter_to_num = ord(letter)
# # print(letter_to_num)
# # print(chr(letter_to_num))
# #
# # for idx, string in enumerate(number):
# #     print(type(idx), type(string))
# #
# # number // (num_1 + num_2) == 1
# #
# # print(3 // (1+1))
# num_men = int(input())
# num_women = int(input())
# max_tables = int(input())
#
#
# def generate_meetings(num_men, num_women, max_tables):
#     tables = min(num_men, num_women, max_tables)
#     print(tables)
#     possible_meetings = 0
#     for table in range(1, tables + 1):
#         for seat1 in range(1, 3):
#             for seat2 in range(seat1 + 1, 4):
#                 # Проверяваме дали остават достатъчно клиенти за среща
#                 if num_men > 0 and num_women > 0:
#                     print(f"({seat1}{table} <-> {seat2}{table})", end=" ")
#                     possible_meetings += 1

# letter = input()
# letter_count = ord(letter)
# print(letter_count)
# print(chr(letter_count))
number = int(input())
print(chr(number))