hour = int(input())
minutes = int(input())

new_time= hour * 60 + minutes +15
hour_new = new_time // 60
minutes_new = new_time % 60

if hour_new == 24:
    hour_new = 0

print (f"{hour_new}:{minutes_new:02d}")
