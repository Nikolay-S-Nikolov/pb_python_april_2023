exam_hrs = int(input())
exam_min = int(input())
arrival_hrs = int(input())
arrival_min = int(input())

exam_time = exam_hrs * 60 + exam_min
arrival_time = arrival_hrs * 60 + arrival_min
difference_time = exam_time - arrival_time

if difference_time < 0:
    print("Late")
    if difference_time > -60:
        print(f"{abs(difference_time)} minutes after the start")
    else:
        hh = abs(difference_time) // 60
        mm = abs(difference_time) % 60
        print(f"{hh}:{mm:02d} hours after the start")
elif 30 >= difference_time >= 0:
    print("On time")
    if difference_time != 0:
        print(f"{difference_time} minutes before the start")
elif 30 < difference_time:
    print("Early")
    if difference_time < 60:
        print(f"{difference_time} minutes before the start")
    else:
        hh = difference_time // 60
        mm = difference_time % 60
        print(f"{hh}:{mm:02d} hours before the start")
