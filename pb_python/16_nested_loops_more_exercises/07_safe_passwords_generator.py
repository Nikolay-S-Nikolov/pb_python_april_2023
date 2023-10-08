number_a = int(input())
number_b = int(input())
max_generated_password = int(input())
symbol_A = 35
symbol_B = 64
generated_password_count = 0
for symbol_x in range(1, number_a + 1):
    for symbol_y in range(1, number_b + 1):
        if symbol_A == 56:
            symbol_A = 35
        if symbol_B == 97:
            symbol_B = 64
        if max_generated_password == generated_password_count:
            break
        print(f"{chr(symbol_A)}{chr(symbol_B)}{symbol_x}{symbol_y}{chr(symbol_B)}{chr(symbol_A)}|", end="")
        generated_password_count += 1
        symbol_A += 1
        symbol_B += 1
