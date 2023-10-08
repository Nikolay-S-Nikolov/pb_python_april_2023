END_COMMAND = "Done"
width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())
volume_free_pace = width_free_space * length_free_space * height_free_space
number_boxes = 0
command = input()

while not command == END_COMMAND:
    number_boxes += int(command)
    if number_boxes >= volume_free_pace:
        print(f"No more free space! You need {number_boxes - volume_free_pace} Cubic meters more.")
        break
    command = input()
else:
    print(f"{volume_free_pace - number_boxes} Cubic meters left.")
