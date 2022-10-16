budget = float(input())
category = input()
people = int(input())
price_vip = 499.99
price_normal = 249.99
transport = 0
if 1 <= people <= 4:
    transport = budget * 0.75
elif 5 <= people <= 9:
    transport = budget * 0.60
elif 10 <= people <= 24:
    transport = budget * 0.50
elif 25 <= people <= 49:
    transport = budget * 0.40
elif people >= 50:
    transport = budget * 0.25
if category == 'Normal':
    price = price_normal * people
elif category == 'VIP':
    price = price_vip * people
total_price = price + transport
difference = abs(budget - (price + transport))
if budget < total_price:
    print(f'Not enough money! You need{difference: .2f} leva.')
else:
    print(f'Yes! You have{difference: .2f} leva left.')