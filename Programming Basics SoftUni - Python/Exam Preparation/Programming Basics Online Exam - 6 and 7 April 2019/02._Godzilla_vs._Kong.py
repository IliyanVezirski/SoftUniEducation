budget = float(input())
extras = int(input())
price_for_dress_for_extras = float(input())
price_for_extras = price_for_dress_for_extras * extras
decor_price = budget * 0.10
if extras > 150:
    price_for_extras *= 0.90
total = decor_price + price_for_extras
diff = abs(budget - total)
if budget >= total:
    print(f'Action!')
    print(f'Wingard starts filming with {diff:.2f} leva left.')
else:
    print(f'Not enough money!')
    print(f'Wingard needs {diff:.2f} leva more.')