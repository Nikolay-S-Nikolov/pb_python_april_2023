NOMINATION_POINTS = 1250.5

actor = input()
starting_points = float(input())
judges_count = int(input())
total_points = starting_points

for _ in range(judges_count):
    judge_name = input()
    judge_points = float(input())
    total_points += len(judge_name) * judge_points / 2
    if total_points > NOMINATION_POINTS:
        break

if total_points > NOMINATION_POINTS:
    print(f"Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!")
else:
    print(f"Sorry, {actor} you need {NOMINATION_POINTS - total_points:.1f} more!")
