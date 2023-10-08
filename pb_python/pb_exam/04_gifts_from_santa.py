num_n = int(input())
num_m = int(input())
num_s = int(input())

for address_number in range(num_m, num_n, -1):
    if address_number % 2 != 0 or address_number % 3 != 0:
        continue
    elif address_number == num_s:
        break
    else:
        print(f"{address_number}", end=" ")
