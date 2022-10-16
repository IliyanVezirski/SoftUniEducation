joinery_number =int(input())
joinery_type = input()
with_delivery_or_not =input()
total = 0
price = 0
if joinery_number < 10:
    print(f'Invalid order')
else:
    if joinery_type == '90X130':
        price = 110
        if 30 < joinery_number <= 60:
            price *= 0.95
        elif joinery_number > 60:
            price *= 0.92
    elif joinery_type == '100X150':
        price = 140
        if 40 < joinery_number <= 80:
            price *= 0.94
        elif joinery_number > 80:
            price *= 0.90
    elif joinery_type == '130X180':
        price = 190
        if 20 < joinery_number <= 50:
            price *= 0.93
        elif joinery_number > 50:
            price *= 0.88
    elif joinery_type == '200X300':
        price = 250
        if 25 < joinery_number <= 50:
            price *= 0.91
        elif joinery_number > 50:
            price *= 0.86
    if with_delivery_or_not == 'With delivery':
        total = price * joinery_number + 60
    else:
        total = price * joinery_number
    if joinery_number > 99:
        total *= 0.96
    print(f'{total:.2f} BGN')
