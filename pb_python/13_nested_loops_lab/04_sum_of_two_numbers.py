start_number = int(input())
end_number = int(input())
magic_number = int(input())
combination_1 = start_number
combination = 0
magic_number_combination = 0
for combination_1 in range(start_number, end_number+1):
    for combination_2 in range(start_number, end_number+1):
        combination += 1
        if (combination_1 + combination_2) == magic_number:
            magic_number_combination = combination
            print(f"Combination N:{combination} ({combination_1} + {combination_2} = {magic_number})")
            break
    if not magic_number_combination == 0:
        break
if magic_number_combination == 0:
    print(f"{combination} combinations - neither equals {magic_number}")
