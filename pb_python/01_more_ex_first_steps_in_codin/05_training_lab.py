length_w = float(input())
width_h = float(input())

useful_width = width_h - 1.00
rows = useful_width // 0.70
column = length_w // 1.20
seats = rows * column - 3
print(int(seats))
