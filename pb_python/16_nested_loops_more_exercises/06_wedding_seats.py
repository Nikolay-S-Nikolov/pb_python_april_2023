last_sector_letter = input()
first_sector_rows_numbers = int(input())
seat_odd_row_numbers = int(input())
rows_numbers = first_sector_rows_numbers
seats_count = 0
sector_last_letter = ord(last_sector_letter)
for sector_letter_in_number in range(65, sector_last_letter + 1):
    for row_count in range(1, rows_numbers + 1):
        if row_count % 2 == 0:
            seat_numbers = seat_odd_row_numbers + 2
        else:
            seat_numbers = seat_odd_row_numbers
        for seat_number in range(97, 97 + seat_numbers):
            seats_count += 1
            print(f"{chr(sector_letter_in_number)}{row_count}{chr(seat_number)}")
    rows_numbers += 1
print(seats_count)
