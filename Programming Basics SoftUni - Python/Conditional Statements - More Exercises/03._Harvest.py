import math
area = int(input())
grapes_from_square = float(input())
needed_wine = int(input())
workers = int(input())
area_for_wine = area * 0.40
liter_wine = (area_for_wine * grapes_from_square) / 2.5
wine_defference = abs(needed_wine - liter_wine)
liter_per_worker = wine_defference / workers
if needed_wine > liter_wine:
    print(f'It will be a tough winter! More {math.floor(wine_defference)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(liter_wine)} liters.')
    print(f'{math.ceil(wine_defference)} liters left -> {math.ceil(liter_per_worker)} liters per person.')