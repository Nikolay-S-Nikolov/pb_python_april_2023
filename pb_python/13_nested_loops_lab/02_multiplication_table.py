first_multiplier = 1
second_multiplier = 1

while first_multiplier < 11:
    second_multiplier = 1
    while second_multiplier < 11:
        quotient = first_multiplier * second_multiplier
        print(f"{first_multiplier} * {second_multiplier} = {quotient}")
        second_multiplier += 1
    first_multiplier += 1

# for first_multiplier in range(1, 11):
#     for second_multiplier in range(1, 11):
#         quotient = first_multiplier * second_multiplier
#         print(f"{first_multiplier} * {second_multiplier} = {quotient}")
