shipment_weight = float(input())
service_type = input()  # standard, express
distance_km = int(input())
distance_km_price = 0
shipping_cost = 0

if service_type == "standard":
    if shipment_weight < 1:
        distance_km_price = 3
    elif 1 <= shipment_weight < 10:
        distance_km_price = 5
    elif 10 <= shipment_weight < 40:
        distance_km_price = 10
    elif 40 <= shipment_weight < 90:
        distance_km_price = 15
    elif 90 <= shipment_weight < 150:
        distance_km_price = 20
    shipping_cost = distance_km_price * distance_km
    shipping_cost_lv = shipping_cost / 100

if service_type == "express":
    if shipment_weight < 1:
        distance_km_price = 3
        overpriced = 0.80
    elif 1 <= shipment_weight < 10:
        distance_km_price = 5
        overpriced = 0.40
    elif 10 <= shipment_weight < 40:
        distance_km_price = 10
        overpriced = 0.05
    elif 40 <= shipment_weight < 90:
        distance_km_price = 15
        overpriced = 0.02
    elif 90 <= shipment_weight < 150:
        distance_km_price = 20
        overpriced = 0.01
    overpriced_km = distance_km_price * overpriced
    shipping_cost = (distance_km_price * distance_km) + (overpriced_km * shipment_weight)
    shipping_cost_lv = shipping_cost / 100

print(f"The delivery of your shipment with weight of {shipment_weight:.3f} kg. would cost {shipping_cost_lv:.2f} lv.")