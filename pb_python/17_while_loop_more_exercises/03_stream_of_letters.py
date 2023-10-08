command = input()

is_letter_o = False
is_letter_n = False
is_letter_c = False
word = ""
while not command == "End":
    number = ord(command)
    if 64 < number < 91 or 96 < number < 123:
        command = chr(number)
    else:
        command = input()
        continue
    if command == "o":
        if is_letter_o:
            word += command
        else:
            is_letter_o = True
    elif command == "n":
        if is_letter_n:
            word += command
        else:
            is_letter_n = True
    elif command == "c":
        if is_letter_c:
            word += command
        else:
            is_letter_c = True
    else:
        word += command
    if is_letter_c and is_letter_n and is_letter_o:
        print(word, end=" ")
        is_letter_o = False
        is_letter_n = False
        is_letter_c = False
        word = ""
        command = input()
        continue
    command = input()
