command = input()
adults_number = 0
kids_number = 0
while not command == "Christmas":
    age = int(command)
    if age > 16:
        adults_number += 1
    else:
        kids_number += 1
    command = input()
toys_price = kids_number * 5
sweaters_price = adults_number * 15
print(f"Number of adults: {adults_number}")
print(f"Number of kids: {kids_number}")
print(f"Money for toys: {toys_price}")
print(f"Money for sweaters: {sweaters_price}")
