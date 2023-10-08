number_n = int(input())
number_count = 0
left_sum = 0
right_sum = 0
for two_times_n in range(2 * number_n):
    number_2n = int(input())
    number_count += 1
    if number_count <= number_n:
        left_sum += number_2n
    else:
        right_sum += number_2n
if left_sum == right_sum:
    print(f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")
