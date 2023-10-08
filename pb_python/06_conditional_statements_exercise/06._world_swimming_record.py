record_sec = float(input())
distance_meters = float(input())
sec_for_1_m = float(input())

time_swam = distance_meters * sec_for_1_m
time_swam_with_resistance = (distance_meters // 15) * 12.5 + time_swam

if time_swam_with_resistance < record_sec:
    print(f" Yes, he succeeded! The new world record is {time_swam_with_resistance:.2f} seconds.")
else:
    sec_slower = time_swam_with_resistance - record_sec
    print(f"No, he failed! He was {sec_slower:.2f} seconds slower.")
