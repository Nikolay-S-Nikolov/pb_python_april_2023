number_m = int(input())
print_counter = 0
password_first_number = 0
password_second_num = 0
password_third_num = 0
password_forth_num = 0
password_found = False
for first_num in range(1, 10):
    for second_num in range(1, 10):
        for third_num in range(1, 10):
            for forth_num in range(1, 10):
                if first_num * second_num + third_num * forth_num == number_m:
                    if second_num > first_num and third_num > forth_num:
                        print_counter += 1
                        print(f"{first_num}{second_num}{third_num}{forth_num}", end=" ")
                        if print_counter == 4:
                            password_found = True
                            password_first_number = first_num
                            password_second_num = second_num
                            password_third_num = third_num
                            password_forth_num = forth_num
print()
if password_found:
    print(f"Password: {password_first_number}{password_second_num}{password_third_num}{password_forth_num}")
else:
    print("No!")
