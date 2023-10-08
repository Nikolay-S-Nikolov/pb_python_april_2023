WRAPPING_PAPER = 5.80
CLOTH = 7.20
GLUE_LTR = 1.20

wrapping_paper_count = int(input())
cloth_count = int(input())
liters_glue = float(input())
discount_percentage = int(input())

total_price = wrapping_paper_count * WRAPPING_PAPER \
              + cloth_count * CLOTH \
              + liters_glue * GLUE_LTR

needed_money = total_price * (1 - discount_percentage / 100)

print(f"{needed_money:.3f}")
