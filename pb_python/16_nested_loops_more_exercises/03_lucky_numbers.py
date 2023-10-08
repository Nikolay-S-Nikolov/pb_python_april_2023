number = int(input())
for num_1 in range(1, 10):
    for num_2 in range(1, 10):
        for num_3 in range(1, 10):
            for num_4 in range(1, 10):
                if num_1 + num_2 == num_3 + num_4 and number % (num_1 + num_2) == 0:
                    print(f"{num_1}{num_2}{num_3}{num_4}", end=" ")
