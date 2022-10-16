drink = input()
with_sugar_or_not = input()
drink_number = int(input())
price = 0
if drink == 'Espresso':
    if with_sugar_or_not == 'Without':
        price = 0.90
    elif with_sugar_or_not == 'Normal':
        price = 1
    elif with_sugar_or_not == 'Extra':
        price = 1.20
elif drink == 'Cappuccino':
    if with_sugar_or_not == 'Without':
        price = 1
    elif with_sugar_or_not == 'Normal':
        price = 1.20
    elif with_sugar_or_not == 'Extra':
        price = 1.60
elif drink == 'Tea':
    if with_sugar_or_not == 'Without':
        price = 0.50
    elif with_sugar_or_not == 'Normal':
        price = 0.60
    elif with_sugar_or_not == 'Extra':
        price = 0.70
total = price * drink_number
if with_sugar_or_not == 'Without':
    total *= 0.65
if drink == 'Espresso' and drink_number >= 5:
    total *= 0.75
if total > 15:
    total *= 0.80
print(f'You bought {drink_number} cups of {drink} for {total:.2f} lv.')