command = input()
min_number = float("inf")

while command != "Stop":
    number = int(command)
    if number < min_number:
        min_number = number
    command = input()
print(min_number)
