number_1 = int(input())  # number_1 < number_2
number_2 = int(input())

for search in range(number_1, number_2 + 1):
    idx_look = str(search)
    odd_sum = 0
    even_sum = 0
    for idx, num in enumerate(idx_look):
        if idx % 2 == 0 or idx == 0:
            odd_sum += int(num)
        else:
            even_sum += int(num)
    if odd_sum == even_sum:
        print(idx_look, end=" ")
