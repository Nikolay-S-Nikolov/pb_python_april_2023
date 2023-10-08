input_text = input()
value = 0
for t_string in input_text:
    if t_string == "a":
        value += 1
    if t_string == "e":
        value += 2
    if t_string == "i":
        value += 3
    if t_string == "o":
        value += 4
    if t_string == "u":
        value += 5
print(value)