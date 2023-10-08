import sys
number_n = int(input())
max_number = -  sys.maxsize
min_number = sys.maxsize
for compare_n in range(number_n):
    inp_number = int(input())
    if inp_number > max_number:
        max_number = inp_number
    if inp_number < min_number:
        min_number = inp_number
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
