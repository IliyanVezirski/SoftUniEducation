days = int(input())
food = float(input())
cat_food = 0
dog_food = 0
dog_eaten_food = 0
cat_eaten_food = 0
biscuits_for_the_day = 0
biscuits_total = 0
eaten_food = 0
for foods in range(1, days + 1):
    dog_food = float(input())
    cat_food = float(input())
    dog_eaten_food += dog_food
    cat_eaten_food += cat_food
    if foods % 3 == 0:
        biscuits_for_the_day = (dog_food + cat_food) * 0.10
        biscuits_total += biscuits_for_the_day
eaten_food = dog_eaten_food + cat_eaten_food
percentage_eaten_food = ('%.2f' % ((dog_eaten_food + cat_eaten_food) / food * 100))
percentage_dog = ('%.2f' % (dog_eaten_food / eaten_food * 100))
percentage_cat = ('%.2f' % (cat_eaten_food / eaten_food * 100))
print(f"Total eaten biscuits: {round(biscuits_total)}gr.")
print(f"{percentage_eaten_food}% of the food has been eaten.")
print(f'{percentage_dog}% eaten from the dog.')
print(f'{percentage_cat}% eaten from the cat.')