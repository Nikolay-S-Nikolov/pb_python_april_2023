experts_number = int(input())
presentation_name = input()
all_presentation_score_sum = 0
presentation_count = 0
while not presentation_name == "Finish":
    presentation_count += 1
    sum_score = 0
    for _ in range(experts_number):
        score = float(input())
        sum_score += score
    average_score = sum_score / experts_number
    print(f"{presentation_name} - {average_score:.2f}.")
    all_presentation_score_sum += average_score
    presentation_name = input()

all_presentation_average_score = all_presentation_score_sum / presentation_count
print(f"Student's final assessment is {all_presentation_average_score:.2f}.")  # after command "Finish"
