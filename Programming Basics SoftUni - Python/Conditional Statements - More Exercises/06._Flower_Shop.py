import math
magnolia = int(input())
zumbul = int(input())
roses = int(input())
cactus = int(input())
price_for_present = float(input())
income_magnolia = magnolia * 3.25
income_zumbul = zumbul * 4
income_roses = roses * 3.5
income_cactus = cactus * 8
income = (income_cactus + income_zumbul + income_roses + income_magnolia) * 0.95
income_difference = abs(price_for_present - income)
if income >= price_for_present:
    print(f'She is left with {math.floor(income_difference)} leva.')
else:
    print(f'She will have to borrow {math.ceil(income_difference)} leva.')