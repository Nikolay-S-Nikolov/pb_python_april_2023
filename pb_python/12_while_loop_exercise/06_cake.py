cake_width = int(input())
cake_length = int(input())
cake_pieces = cake_length * cake_width
command = input()
pieces_taken = 0
taken=0
while not command == "STOP":
    taken = int(command)
    pieces_taken += taken
    if pieces_taken >= cake_pieces:
        print(f"No more cake left! You need {(pieces_taken-cake_pieces)} pieces more.")
        break
    command = input()
else:
    print(f"{(cake_pieces-pieces_taken)} pieces are left.")
