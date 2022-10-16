flower = input()
flower_quantity = int(input())
budget = int(input())
if flower == 'Roses':
    total_price = flower_quantity * 5
    if flower_quantity > 80:
        total_price *= 0.90
elif flower == 'Dahlias':
    total_price = flower_quantity * 3.80
    if flower_quantity > 90:
        total_price *= 0.85
elif flower == 'Tulips':
    total_price = flower_quantity * 2.80
    if flower_quantity > 80:
        total_price *= 0.85
elif flower == 'Narcissus':
    total_price = flower_quantity * 3
    if flower_quantity < 120:
        total_price *= 1.15
elif flower == 'Gladiolus':
    total_price = flower_quantity * 2.50
    if flower_quantity < 80:
        total_price *= 1.20
difference = abs(budget - total_price)
difference = ('% .2f' % difference)
if budget >= total_price:
    print('Hey, you have a great garden with ' + str(flower_quantity) + ' ' + str(flower) + ' and' + str(difference) + ' leva left.')
else:
    print('Not enough money, you need' + str(difference) + ' leva more.')