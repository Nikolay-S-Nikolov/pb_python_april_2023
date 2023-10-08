# Ред 1.	Малка буква от английската азбука за начало на интервала – от ‘a’ до ‚z’.
# Ред 2.	Малка буква от английската азбука за край на интервала  – от първата буква до ‚z’.
# Ред 3.	Малка буква от английската азбука – от ‘a’ до ‚z’ – като комбинациите съдържащи тази буквата се пропускат.
small_letter_1_a_to_z = ord(input())
small_letter_2_a_to_z = ord(input())
small_letter_3_a_to_z = ord(input())
print_counter = 0
for letter_1 in range(small_letter_1_a_to_z, small_letter_2_a_to_z + 1):
    if letter_1 == small_letter_3_a_to_z:
        continue
    for letter_2 in range(small_letter_1_a_to_z, small_letter_2_a_to_z + 1):
        if letter_2 == small_letter_3_a_to_z:
            continue
        for letter_3 in range(small_letter_1_a_to_z, small_letter_2_a_to_z + 1):
            if letter_3 == small_letter_3_a_to_z:
                continue
            num_letter1 = chr(letter_1)
            num_letter2 = chr(letter_2)
            num_letter3 = chr(letter_3)
            print_counter += 1
            print(f"{num_letter1}{num_letter2}{num_letter3}", end=" ")
print(print_counter)
