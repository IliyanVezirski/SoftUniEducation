budget = float(input())
serials_number = int(input())
total_price = 0
for serials in range(serials_number):
    name_serial = input()
    price = float(input())
    if name_serial == 'Thrones':
        price *= 0.50
    elif name_serial == 'Lucifer':
        price *= 0.60
    elif name_serial == 'Protector':
        price *= 0.70
    elif name_serial == 'TotalDrama':
        price *= 0.80
    elif name_serial == 'Area':
        price *= 0.90
    total_price += price
    price = 0
diff = abs(total_price - budget)
if total_price <= budget:
    print(f'You bought all the series and left with {diff:.2f} lv.')
else:
    print(f'You need {diff:.2f} lv. more to buy the series!')