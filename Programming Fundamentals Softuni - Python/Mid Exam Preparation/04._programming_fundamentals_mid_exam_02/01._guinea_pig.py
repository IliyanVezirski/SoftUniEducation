food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
quine_pig_weight = float(input()) * 1000
enough_for_month = True
for day in range(1, 31):
    food -= 300
    if day % 2 == 0:
        hay -= food * 0.05
    if day % 3 == 0:
        cover -= quine_pig_weight / 3
    if food <= 0 or hay <= 0 or cover <= 0:
        print(f"Merry must go to the pet store!")
        enough_for_month = False
        break
if enough_for_month:

    print(f"Everything is fine! Puppy is happy! Food: {food /1000:.2f}, Hay: {hay /1000:.2f}, Cover: {cover / 1000:.2f}.")