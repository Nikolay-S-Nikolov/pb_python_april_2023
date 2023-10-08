from sys import maxsize

numbers_n = int(input())
max_number = -maxsize
input_numbers = 0
sum_numbers = 0
for sum_n in range(numbers_n):
    input_numbers = int(input())
    if input_numbers > max_number:
        max_number = input_numbers
    sum_numbers += input_numbers
if max_number == (sum_numbers - max_number):
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {abs(max_number - (sum_numbers - max_number))}")
