from math import floor

record_sec = float(input())
distance_m = float(input())
meter_per_sec = float(input())

time_without_delay = distance_m * meter_per_sec
delay = (floor(distance_m / 50)) * 30
achieved_time = time_without_delay + delay

if achieved_time < record_sec:
    print(f" Yes! The new record is {achieved_time:.2f} seconds.")  # Aко Георги е подобрил рекорда отпечатваме.
else:
    print(f"No! He was {achieved_time - record_sec:.2f} seconds slower.")  # Ако НЕ е подобрил рекорда отпечатваме.
