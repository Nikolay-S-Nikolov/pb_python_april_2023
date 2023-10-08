from math import ceil

video_card_price = int(input())
transition_price = int(input())
consumed_power_by_video_card_per_day = float(input())
money_gain_one_video_card_per_day = float(input())

total_price_video_card = video_card_price * 13
total_transition_price = transition_price * 13
total_spendings = total_price_video_card + total_transition_price + 1000
money_gained_by_card_per_day = money_gain_one_video_card_per_day - consumed_power_by_video_card_per_day
total_gain_for_all_cards = 13 * money_gained_by_card_per_day
days_to_return_money = total_spendings / total_gain_for_all_cards
print(total_spendings)
print(ceil(days_to_return_money))
