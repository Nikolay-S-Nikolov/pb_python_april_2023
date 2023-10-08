student_name = input()
sum_grade_score = 0
grade_number = 1
repeated_class = 0
is_excluded = False
while grade_number < 13:
    grade_score = float(input())
    if grade_score < 4:
        repeated_class += 1
        if repeated_class > 1:
            is_excluded = True
            break
        continue
    grade_number += 1
    sum_grade_score += grade_score

if is_excluded:
    print(f"{student_name} has been excluded at {grade_number} grade")
else:
    average_grade = sum_grade_score / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
