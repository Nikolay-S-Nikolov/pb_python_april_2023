team_name = input()
souvenir_type = input()
bought_souvenirs_count = int(input())

souvenir_price = 0
correct_souvenir_country = True
if team_name == "Argentina":
    if souvenir_type == "flags":
        souvenir_price = 3.25
    elif souvenir_type == "caps":
        souvenir_price = 7.20
    elif souvenir_type == "posters":
        souvenir_price = 5.10
    elif souvenir_type == "stickers":
        souvenir_price = 1.25
    else:
        correct_souvenir_country = False
        print("Invalid stock!")
elif team_name == "Brazil":
    if souvenir_type == "flags":
        souvenir_price = 4.20
    elif souvenir_type == "caps":
        souvenir_price = 8.50
    elif souvenir_type == "posters":
        souvenir_price = 5.35
    elif souvenir_type == "stickers":
        souvenir_price = 1.20
    else:
        correct_souvenir_country = False
        print("Invalid stock!")
elif team_name == "Croatia":
    if souvenir_type == "flags":
        souvenir_price = 2.75
    elif souvenir_type == "caps":
        souvenir_price = 6.90
    elif souvenir_type == "posters":
        souvenir_price = 4.95
    elif souvenir_type == "stickers":
        souvenir_price = 1.10
    else:
        correct_souvenir_country = False
        print("Invalid stock!")
elif team_name == "Denmark":
    if souvenir_type == "flags":
        souvenir_price = 3.10
    elif souvenir_type == "caps":
        souvenir_price = 6.50
    elif souvenir_type == "posters":
        souvenir_price = 4.80
    elif souvenir_type == "stickers":
        souvenir_price = 0.90
    else:
        correct_souvenir_country = False
        print("Invalid stock!")
else:
    correct_souvenir_country = False
    print("Invalid country!")

if correct_souvenir_country:
    total_amount = souvenir_price*bought_souvenirs_count
    print(f"Pepi bought {bought_souvenirs_count} {souvenir_type} of {team_name} for {total_amount:.2f} lv.")
