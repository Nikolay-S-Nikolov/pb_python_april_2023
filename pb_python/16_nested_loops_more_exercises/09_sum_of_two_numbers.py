interval_start = int(input())
interval_end = int(input())
magic_number = int(input())

combination_number = 0
no_magic_number = True
for first_number in range(interval_start, interval_end + 1):
    if not no_magic_number:
        break
    for second_number in range(interval_start, interval_end + 1):
        combination_number+=1
        if first_number+second_number == magic_number:
            print(f"Combination N:{combination_number} ({first_number} + {second_number} = {magic_number})")
            no_magic_number = False
            break
if no_magic_number:
    print(f"{combination_number} combinations - neither equals {magic_number}")
