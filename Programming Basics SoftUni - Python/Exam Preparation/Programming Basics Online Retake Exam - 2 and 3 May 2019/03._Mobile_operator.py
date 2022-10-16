term = input()
type_contract = input()
mobile_internet = input()
months_to_pay = int(input())
price = 0
internet_price = 0
if term == 'one':
    if type_contract == 'Small':
        price = 9.98
    elif type_contract == 'Middle':
        price = 18.99
    elif type_contract == 'Large':
        price = 25.98
    elif type_contract == 'ExtraLarge':
        price = 35.99
elif term == 'two':
    if type_contract == 'Small':
        price = 8.58
    elif type_contract == 'Middle':
        price = 17.09
    elif type_contract == 'Large':
        price = 23.59
    elif type_contract == 'ExtraLarge':
        price = 31.79
if mobile_internet == 'yes':
    if price <= 10:
        internet_price = 5.5
    elif 10 < price <= 30:
        internet_price = 4.35
    elif price > 30:
        internet_price = 3.85
price = price + internet_price
if term == 'two':
    price *= 0.9625
total = price * months_to_pay
print(f'{total:.2f} lv.')
