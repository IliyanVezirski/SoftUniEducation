bottles = int(input())
mililiters = bottles * 750
counter = 0
dishes_sum = 0
pot_sum = 0
plate_sum = 0
while mililiters >= 0:
    dishes = input()
    if dishes == 'End':
        break
    else:
        dishes = int(dishes)
    dishes_sum += dishes
    counter += 1
    if counter % 3 == 0:
        mililiters = mililiters - (dishes * 15)
        pot_sum += dishes
    else:
        mililiters = mililiters - (dishes * 5)
        plate_sum += dishes
if mililiters >= 0:
    print('Detergent was enough!')
    print(f'{plate_sum} dishes and {pot_sum} pots were washed.')
    print(f'Leftover detergent {mililiters} ml.')
else:
    print(f'Not enough detergent, {abs(mililiters)} ml. more necessary!')
