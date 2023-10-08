control_min = int(input())
control_sec = int(input())
length_chute_meters = float(input())
sec_for_100_meters = int(input())

control_time = control_min * 60 + control_sec
friction_delay_time = (length_chute_meters / 120) * 2.5
martin_time = (length_chute_meters / 100) * sec_for_100_meters - friction_delay_time

if martin_time <= control_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {martin_time:.3f}.")
else:
    print(f"No, Marin failed! He was {martin_time - control_time:.3f} second slower.")
