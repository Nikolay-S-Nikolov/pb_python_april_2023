number_n = int(input())
number_count = 0
even_sum = 0
odd_sum = 0
for new_input_numbers in range(number_n):
    number_inp = int(input())
    number_count += 1
    if number_count % 2 == 0:
        even_sum += number_inp
    else:
        odd_sum += number_inp
if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {even_sum}")
else:
    print("No")
    print(f"Diff = {abs(even_sum - odd_sum)}")
