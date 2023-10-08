tournament_days_count = int(input())
total_win_gain = 0
all_win_count = 0
all_loose_count = 0
for days in range(tournament_days_count):
    win_count = 0
    lose_count = 0
    win_gain = 0
    command = input()
    while not command == "Finish":
        sport = command
        result = input()  # "win" or "lose"
        if result == "win":
            win_count += 1
            all_win_count += 1
            win_gain += 20
        elif result == "lose":
            lose_count += 1
            all_loose_count += 1
        command = input()
    if win_count > lose_count:
        total_win_gain += win_gain + win_gain * 0.1
    else:
        total_win_gain += win_gain
if all_win_count > all_loose_count:
    total_win_gain += total_win_gain * 0.2
    print(f"You won the tournament! Total raised money: {total_win_gain:.2f}")  # Ако сте спечелили турнира
else:
    print(f"You lost the tournament! Total raised money: {total_win_gain:.2f}")  # Ако сте загубили на турнира
