detergent_bottles_count = int(input())
command = input()

left_detergent = detergent_bottles_count * 750
counter = 0
clean_plates_count = 0
clean_pots_count = 0
while not command == "End":
    dishes = int(command)
    counter += 1
    if not counter % 3 == 0:
        clean_plates_count += dishes
        left_detergent -= dishes * 5
    else:
        clean_pots_count += dishes
        left_detergent -= dishes * 15
    if left_detergent < 0:
        break
    command = input()

if left_detergent >= 0:
    print("Detergent was enough!")
    print(f"{clean_plates_count} dishes and {clean_pots_count} pots were washed.")
    print(f"Leftover detergent {left_detergent} ml.")
else:
    print(f"Not enough detergent, {abs(left_detergent)} ml. more necessary!")
