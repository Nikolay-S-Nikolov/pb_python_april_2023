# num1 = int(input())
# num2 = int(input())
# num = num1 % num2
# print(num)
# num = 543210
# str_num = str(num)
# for index, number in enumerate(str_num):
#     if index==2:
#         print(index)
#         print (number)

# command1 = input()  # "End" or 11
#
# while command1 != "End":
#     command_new = int(command1)
#     print(type(command_new))
#     command1 = input()
command = input()  # Can be "Finish" or movie name

student_ticket_count = 0
standard_ticket_count = 0
kid_ticket_count = 0
seats = 0
movie_name = ""
while not command == "Finish":
    seats = int(input())
    tickets_count = 0
    it_is_end = False
    while True:
        movie_name = command
        ticket_type = input()  # Can be "student", "standard" or "kid"
        if ticket_type == "End":
            it_is_end = True
            break
        tickets_count += 1
        if ticket_type == "student":
            student_ticket_count += 1
        elif ticket_type == "standard":
            standard_ticket_count += 1
        elif ticket_type == "kid":
            kid_ticket_count += 1
        if tickets_count == seats:
            it_is_end = True
            break
    if it_is_end:
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
