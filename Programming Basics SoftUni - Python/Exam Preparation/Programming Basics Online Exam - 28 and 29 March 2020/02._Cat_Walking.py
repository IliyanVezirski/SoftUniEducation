walk_minutes_day = int(input())
walks_per_day = int(input())
cat_caloreis = int(input())
calories_burned = walk_minutes_day * 5
calories_burned_per_day = calories_burned * walks_per_day
needed_calories_per_day = cat_caloreis / 2
if calories_burned_per_day >= needed_calories_per_day:
    print (f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned_per_day}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned_per_day}.")