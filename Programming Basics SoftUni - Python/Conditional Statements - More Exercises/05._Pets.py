import math
days = int(input())
food = int(input())
food_for_dog_per_day = float(input())
food_for_cat_per_day = float(input())
food_for_turtle_per_day = float(input()) / 1000
food_needed = food_for_turtle_per_day * days + food_for_cat_per_day * days + food_for_dog_per_day * days
food_difference = abs(math.floor(food - food_needed))
if food >= food_needed:
    print(f"{food_difference} kilos of food left.")
else:
    print(f'{food_difference} more kilos of food are needed.')