number_floors = int(input())
number_rooms = int(input())
room_letter = ""
for current_floor in range(number_floors, 0, -1):
    if current_floor == number_floors:
        room_letter = "L"
    elif current_floor % 2 == 0:
        room_letter = "O"
    else:
        room_letter = "A"
    for current_room in range(number_rooms):
        print(f"{room_letter}{current_floor}{current_room}", end=" ")
    print()
