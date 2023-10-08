from math import ceil

serial_name = input()
serial_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
recreation_time = break_duration / 4

time_left = break_duration - lunch_time - recreation_time

extra_time = serial_duration - time_left
extra_time = ceil(abs(extra_time))
if time_left >= serial_duration:
    print(f"You have enough time to watch {serial_name} and left with {extra_time} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {extra_time} more minutes.")
