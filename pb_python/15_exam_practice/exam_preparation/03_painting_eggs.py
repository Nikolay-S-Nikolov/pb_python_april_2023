eggs_size = input()  # "Large", "Medium" или "Small"
eggs_color = input()  # "Red", "Green" или "Yellow"
lots_number = int(input())
lot_price = 0
if eggs_size == "Large":
    if eggs_color == "Red":
        lot_price = 16
    elif eggs_color == "Green":
        lot_price = 12
    elif eggs_color == "Yellow":
        lot_price = 9
elif eggs_size == "Medium":
    if eggs_color == "Red":
        lot_price = 13
    elif eggs_color == "Green":
        lot_price = 9
    elif eggs_color == "Yellow":
        lot_price = 7
elif eggs_size == "Small":
    if eggs_color == "Red":
        lot_price = 9
    elif eggs_color == "Green":
        lot_price = 8
    elif eggs_color == "Yellow":
        lot_price = 5

end_price = lots_number*lot_price*(1-0.35)
print(f"{end_price:.2f} leva.")
