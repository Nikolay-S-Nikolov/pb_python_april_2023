import math

tournaments_count = int(input())
starting_points = int(input())
win_points = 0
tournament_won = 0
for _ in range(tournaments_count):
    tournament_stage = input()
    if tournament_stage == "W":
        tournament_won += 1
        win_points += 2000
    elif tournament_stage == "F":
        win_points += 1200
    elif tournament_stage == "SF":
        win_points += 720
final_points = win_points + starting_points
average_points = win_points / tournaments_count
average_points = math.floor(average_points)
percentage_win = tournament_won / tournaments_count * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{percentage_win:.2f}%")
