months = int(input())
water = 20
internet = 15
other = 0
sum_electricity = 0
sum_water = 0
sum_internet = 0
sum_other = 0
for i in range(1, months + 1):
    electricity = float(input())
    sum_electricity += electricity
    sum_water += water
    sum_internet += internet
    other = (electricity + water + internet) * 1.2
    sum_other += other
avarage_bills =('% .2f' % ((sum_electricity + sum_water + sum_internet + sum_other) / months))
print(f'Electricity:{sum_electricity: .2f} lv')
print(f'Water:{sum_water: .2f} lv')
print(f'Internet:{sum_internet: .2f} lv')
print(f'Other:{sum_other: .2f} lv')
print(f'Average:{avarage_bills} lv')