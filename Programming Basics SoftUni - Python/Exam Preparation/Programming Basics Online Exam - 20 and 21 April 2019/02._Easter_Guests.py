import math
guests = int(input())
budget = int(input())
easter_bread_price = 4
egg_price = 0.45
easter_bread_needed = math.ceil(guests / 3)
eggs_needed = guests * 2
easter_bread_total = easter_bread_needed * easter_bread_price
eggs_total = eggs_needed * egg_price
total = eggs_total + easter_bread_total
difference = abs(total - budget)
if total <= budget:
    print(f'Lyubo bought {easter_bread_needed} Easter bread and {eggs_needed} eggs.')
    print(f'He has {difference:.2f} lv. left.')
else:
    print(f"Lyubo doesn't have enough money.")
    print(f'He needs {difference:.2f} lv. more.')