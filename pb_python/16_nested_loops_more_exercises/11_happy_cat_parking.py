days_count = int(input())
hours_count_for_every_day = int(input())

total_payed = 0
pey_per_hour = 0
for day_index in range(1, days_count + 1):
    payment_for_that_day = 0
    for hours in range(1, hours_count_for_every_day + 1):
        if not day_index % 2 == 0 and hours % 2 == 0:
            pey_per_hour = 1.25
        elif day_index % 2 == 0 and not hours % 2 == 0:
            pey_per_hour = 2.50
        else:
            pey_per_hour = 1.00
        payment_for_that_day += pey_per_hour
    print(f"Day: {day_index} - {payment_for_that_day:.2f} leva")
    total_payed += payment_for_that_day

print(f"Total: {total_payed:.2f} leva")
