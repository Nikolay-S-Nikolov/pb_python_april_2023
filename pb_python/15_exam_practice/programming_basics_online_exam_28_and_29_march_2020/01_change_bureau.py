BITCOIN_TO_LV = 1168.00
CNY_TO_USD = 0.15
USD_TO_LV = 1.76
EUR_TO_LV = 1.95

bitcoins = int(input())
chinese_yuan = float(input())
exchange_commission = float(input())

btc_to_lv = bitcoins * BITCOIN_TO_LV
cny_to_usd = chinese_yuan * CNY_TO_USD
usd_to_lv = cny_to_usd * USD_TO_LV
lv_to_eur = ((btc_to_lv + usd_to_lv) / EUR_TO_LV) * (1 - exchange_commission / 100)
print(f"{lv_to_eur:.2f}")
