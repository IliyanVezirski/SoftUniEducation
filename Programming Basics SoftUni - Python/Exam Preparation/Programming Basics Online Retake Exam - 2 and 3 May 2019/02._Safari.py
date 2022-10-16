budget = float(input())
gasoline_litres_needed = float(input())
day = input()
gasoline_price = gasoline_litres_needed * 2.1
total_price = gasoline_price + 100
if day == 'Saturday':
    total_price *= 0.90
elif day == 'Sunday':
    total_price *= 0.80
diff = abs(budget - total_price)
if budget >= total_price:
    print(f'Safari time! Money left: {diff:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {diff:.2f} lv.')