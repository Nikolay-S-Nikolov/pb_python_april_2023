WALKING_GOAL = 10_000
step_command = input()
step_count = 0
total_steps = 0
while step_command != "Going home":
    step_count = int(step_command)
    total_steps += step_count
    if total_steps >= WALKING_GOAL:
        print(f"Goal reached! Good job!")
        print(f"{(total_steps - WALKING_GOAL)} steps over the goal!")
        break
    step_command = input()

if step_command == "Going home":
    step_command = int(input())
    total_steps += step_command
    if total_steps >= WALKING_GOAL:
        print(f"Goal reached! Good job!")
        print(f"{(total_steps - WALKING_GOAL)} steps over the goal!")
    else:
        print(f"{(WALKING_GOAL - total_steps)} more steps to reach goal.")
