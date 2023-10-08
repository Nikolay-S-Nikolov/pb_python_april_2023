command = input()  # Can be "Finish" or movie name

student_ticket_count = 0
standard_ticket_count = 0
kid_ticket_count = 0
seats = 0
movie_name = ""
while not command == "Finish":
    seats = int(input())
    tickets_count = 0
    while not command == "End":  # free seats in the movie
        movie_name = command
        ticket_type = input()  # Can be "student", "standard" or "kid"
        if ticket_type == "End":
            percentage_hal_occupancy = tickets_count / seats * 100
            print(f"{movie_name} - {percentage_hal_occupancy:.2f}% full.")
            break
        tickets_count += 1
        if ticket_type == "student":
            student_ticket_count += 1
        elif ticket_type == "standard":
            standard_ticket_count += 1
        elif ticket_type == "kid":
            kid_ticket_count += 1
        if tickets_count == seats:
            percentage_hal_occupancy = tickets_count / seats * 100
            print(f"{movie_name} - {percentage_hal_occupancy:.2f}% full.")
            break
    else:
        percentage_hal_occupancy = tickets_count / seats * 100
        print(f"{movie_name} - {percentage_hal_occupancy:.2f}% full.")
    command = input()

total_tickets = student_ticket_count + standard_ticket_count + kid_ticket_count
percentage_student_tickets = student_ticket_count / total_tickets * 100
percentage_standard_tickets = standard_ticket_count / total_tickets * 100
percentage_kids_tickets = kid_ticket_count / total_tickets * 100

print(f"Total tickets: {total_tickets}")  # to be printed after command "Finish"
print(f"{percentage_student_tickets:.2f}% student tickets.")  # to be printed after command "Finish"
print(f"{percentage_standard_tickets:.2f}% standard tickets.")  # to be printed after command "Finish"
print(f"{percentage_kids_tickets:.2f}% kids tickets.")  # to be printed after command "Finish"
