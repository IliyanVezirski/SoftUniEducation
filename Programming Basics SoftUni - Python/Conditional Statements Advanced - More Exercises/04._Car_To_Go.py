budget = float(input())
season = input()
car = ''
classs = ''
cabrio_price = 0
djip_price = 0
if budget <= 100:
    if season == "Summer":
        classs = 'Economy class'
        cabrio_price = budget * 0.35
        car = 'Cabrio'
    else:
        classs = 'Economy class'
        djip_price = budget * 0.65
        car = 'Jeep'
elif 100 < budget <= 500:
    if season == "Summer":
        classs = "Compact class"
        cabrio_price = budget * 0.45
        car = 'Cabrio'
    else:
        classs = "Compact class"
        djip_price = budget * 0.80
        car = 'Jeep'
elif budget > 500:
    classs = "Luxury class"
    djip_price = budget * 0.90
    car = 'Jeep'
car_price = ('% .2f' % (djip_price + cabrio_price))
print(classs)
print(car + ' -'+(str(car_price)))