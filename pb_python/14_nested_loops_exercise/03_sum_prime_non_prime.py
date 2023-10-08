command = input()  # Can be "stop" or number as string
prime_numbers_sum = 0
non_prime_numbers_sum = 0
while not command == "stop":
    number = int(command)
    if number < 0:
        print("Number is negative.")
        command = input()
        continue
    is_prime = True
    for num in range(2, number):
        if number % num == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers_sum += number
    else:
        non_prime_numbers_sum += number
    command = input()

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")
