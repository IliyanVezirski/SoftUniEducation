city = input()
packet_type = input()
yes_vip_or_not = input()
days = int(input())
price = 0
city_true_or_false = False
total = 0
if days < 1:
    city_true_or_false = True
    print(f'Days must be positive number!')
else:
    if city == 'Bansko' or city == 'Borovets':
        city_true_or_false = True
        if packet_type == 'withEquipment':
            price = 100
            if yes_vip_or_not == 'yes':
                price *= 0.90
        elif packet_type == 'noEquipment':
            price = 80
            if yes_vip_or_not == 'yes':
                price *= 0.95
    if city == 'Varna' or city == 'Burgas':
        city_true_or_false = True
        if packet_type == 'withBreakfast':
            price = 130
            if yes_vip_or_not == 'yes':
                price *= 0.88
        elif packet_type == 'noBreakfast':
            price = 100
            if yes_vip_or_not == 'yes':
                price *= 0.93
    if days > 7:
        days -= 1
    total = price * days
if city_true_or_false and days >= 1:
    print(f'The price is {total:.2f}lv! Have a nice time!')
elif not city_true_or_false and days>= 1:
    print(f'Invalid input!')