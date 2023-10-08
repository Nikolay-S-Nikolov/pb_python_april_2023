VIDEO_CARD_LV = 250

budget = float(input())
video_card_pcs = int(input())
processors_pcs = int(input())
ram_pcs = int(input())

processor_lv = video_card_pcs * VIDEO_CARD_LV * 0.35
ram_lv = video_card_pcs * VIDEO_CARD_LV * 0.10

discount = 0
if video_card_pcs > processors_pcs:
    discount = 0.15

total_amount = VIDEO_CARD_LV * video_card_pcs + processor_lv * processors_pcs + ram_lv * ram_pcs
amount_with_discount = total_amount * (1 - discount)

left_needed = budget - amount_with_discount

if amount_with_discount <= budget:
    print(f"You have {left_needed:.2f} leva left!")
else:
    print(f"Not enough money! You need {- left_needed:.2f} leva more!")
