count_computers = int(input())
accomplished_sales = 0
rating = 0
for _ in range(count_computers):
    number = int(input())
    str_number = str(number)
    size_str = len(str_number)
    mod_str = str_number[:size_str - 1]
    possible_sales = int(mod_str)
    if number % 10 == 2:
        rating += 2
        accomplished_sales += 0
    elif number % 10 == 3:
        rating += 3
        accomplished_sales += possible_sales * 0.50
    elif number % 10 == 4:
        rating += 4
        accomplished_sales += possible_sales * 0.70
    elif number % 10 == 5:
        rating += 5
        accomplished_sales += possible_sales * 0.85
    elif number % 10 == 6:
        rating += 6
        accomplished_sales += possible_sales
mean_rating = rating / count_computers
print(f"{accomplished_sales:.2f}")
print(f"{mean_rating:.2f}")
