food_in_kg = int(input())
food_in_gr = food_in_kg * 1000
food_for_eat = input()
eaten_food = 0
while food_for_eat != 'Adopted':
    eaten_food = int(food_for_eat) + eaten_food
    food_for_eat = input()

difference = abs(food_in_gr - eaten_food)
if eaten_food <= food_in_gr:
    print(f'Food is enough! Leftovers: {difference} grams.')
else:
    print(f'Food is not enough. You need {difference} grams more.')