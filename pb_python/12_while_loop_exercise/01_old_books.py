name_of_book = input()

books_searched = 0
while True:
    insert_command = input()
    if name_of_book == insert_command:
        print(f"You checked {books_searched} books and found it.")
        break
    elif insert_command == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {books_searched} books.")
        break
    else:
        books_searched += 1
