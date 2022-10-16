import math

people = int(input())
tax = float(input())
deck_chairs_price = float(input())
umbrella_price = float(input())
total_tax = people * tax
umbrellas = math.ceil(people / 2)
deck_chairs = math.ceil(people * 0.75)
total_deck_chairs = deck_chairs * deck_chairs_price
total_umbrella = umbrellas * umbrella_price
total = total_tax + total_umbrella + total_deck_chairs
print(f'{total:.2f} lv.')