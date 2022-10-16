cargo_number = float('% 2.f' % (float(input())))
sum_tonnage = 0
price_bus = 0
price_truck = 0
price_train = 0
sum_bus = 0
sum_truck = 0
sum_train = 0
for i in range(1, int(cargo_number) + 1):
    tonnage = int(input())
    sum_tonnage += tonnage
    if tonnage <= 3:
        price_bus = tonnage * 200
        sum_bus += tonnage
    elif 4 <= tonnage <= 11:
        price_truck = tonnage * 175
        sum_truck += tonnage
    elif tonnage >= 12:
        price_train = tonnage * 120
        sum_train += tonnage
avarage_price_per_tonnage = ('% .2f' % (((sum_train * 120) + (sum_bus * 200) + (sum_truck * 175)) / sum_tonnage))
precentage_truck = ('%.2f' % (sum_truck / sum_tonnage * 100))
precentage_train = ('%.2f' % (sum_train / sum_tonnage * 100))
precentage_bus = ('%.2f' % (sum_bus / sum_tonnage * 100))
print(avarage_price_per_tonnage)
print(f'{precentage_bus}%')
print(f'{precentage_truck}%')
print(f'{precentage_train}%')