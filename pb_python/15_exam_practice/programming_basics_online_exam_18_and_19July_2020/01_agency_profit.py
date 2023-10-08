airline_name = input()
adults_tickets_count = int(input())
kids_tickets_count = int(input())
adults_tickets_price = float(input())
service_fee = float(input())

kids_tickets_price_with_fee = adults_tickets_price * 0.30 + service_fee
adults_tickets_price_with_fee = adults_tickets_price + service_fee
total_price = adults_tickets_count * adults_tickets_price_with_fee \
              + kids_tickets_count * kids_tickets_price_with_fee
profit = total_price * 0.20
print(f"The profit of your agency from {airline_name} tickets is {profit:.2f} lv.")
