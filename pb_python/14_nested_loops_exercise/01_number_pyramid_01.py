n = int(input())
current = 1
for row in range(1, n):
    is_bigger = False
    for col in range(1, row):
        if current > n:
            break
        print(str(current) + " ", end="")
        current += 1
    if is_bigger:
        break
    print()
