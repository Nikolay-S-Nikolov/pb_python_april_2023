END_COMMAND = "Enough"
BAD_GRADE = 4

bad_grade_count = int(input())
failed_attempts = 0
is_end_command = False
sum_score = 0
problem_count = 0
last_problem_name = ""
while not failed_attempts == bad_grade_count:
    problem_name = input()
    if problem_name == "Enough":
        is_end_command = True
        break
    last_problem_name = problem_name
    score = int(input())
    problem_count += 1
    if score <= BAD_GRADE:
        failed_attempts += 1
    sum_score += score
average_score = sum_score / problem_count

if is_end_command:
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {problem_count}")
    print(f"Last problem: {last_problem_name}")
else:
    print(f"You need a break, {failed_attempts} poor grades.")
