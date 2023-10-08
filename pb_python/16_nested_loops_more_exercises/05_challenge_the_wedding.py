men_count = int(input())
women_count = int(input())
maximum_table_count = int(input())
possible_meetings = 0
for men in range(1, men_count + 1):
    for women in range(1, women_count + 1):
        print(f"({men} <-> {women})", end=" ")
        if maximum_table_count == possible_meetings:
            break
        possible_meetings += 1
