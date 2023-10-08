# number = int(input())
# counter = 0
# for number_x1 in range(number+1):
#     for number_x2 in range(number+1):
#         for number_x3 in range(number+1):
#             if (number_x1 + number_x2 + number_x3) == number:
#                 counter += 1
# print(counter)
number = int(input())
counter = 0
number_x1 = 0
while number_x1 <= number:
    number_x2 = 0
    while number_x2 <= number:
        number_x3 = 0
        while number_x3 <= number:
            if (number_x1 + number_x2 + number_x3) == number:
                counter += 1
            number_x3 += 1
        number_x2 += 1
    number_x1 += 1
print(counter)
