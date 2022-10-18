"""Merry has a guinea pig named Puppy, that she loves very much. Every month she goes to the nearest pet store and buys him everything he needs – food, hay, and cover.
On the first three lines, you will receive the quantity of food, hay, and cover, which Merry buys for a month (30 days). On the fourth line, you will receive the guinea pig's weight.
Every day Puppy eats 300 gr of food. Every second day Merry first feeds the pet, then gives it a certain amount of hay equal to 5% of the rest of the food. On every third day, Merry puts Puppy cover with a quantity of 1/3 of its weight.
Calculate whether the quantity of food, hay, and cover, will be enough for a month.
If Merry runs out of food, hay, or cover, stop the program!
Input
•	On the first line – quantity food in kilograms - a floating-point number in the range [0.0 – 10000.0]
•	On the second line – quantity hay in kilograms - a floating-point number in the range [0.0 – 10000.0]
•	On the third line – quantity cover in kilograms - a floating-point number in the range [0.0 – 10000.0]
•	On the fourth line – guinea's weight in kilograms - a floating-point number in the range [0.0 – 10000.0]
Output
•	If the food, the hay, and the cover are enough, print:
o	"Everything is fine! Puppy is happy! Food: {excessFood}, Hay: {excessHay}, Cover: {excessCover}."
•	If one of the things is not enough, print:
o	"Merry must go to the pet store!"
The output values must be formatted to the second decimal place!
"""

food_kg = float(input())
hay_kg = float(input())
cover_kg: float = float(input())
guinea_kg = float(input())
happy = True
food_grams = food_kg * 1000
hay_grams = hay_kg * 1000
cover_grams = cover_kg * 1000
guinea_grams = guinea_kg * 1000

for day in range(1, 31):
    food_grams -= 300
    if day % 2 == 0:
        hay_grams -= food_grams * 0.05
    if day % 3 == 0:
        cover_grams -= guinea_grams / 3
    if food_grams <= 0 or hay_grams <= 0 or cover_grams <= 0:
        print(f"Merry must go to the pet store!")
        happy = False
        break

if happy:
    food_kg = food_grams / 1000
    hay_kg = hay_grams / 1000
    cover_kg = cover_grams / 1000
    print(f"Everything is fine! Puppy is happy! Food: {food_kg:.2f}, Hay: {hay_kg:.2f}, Cover: {cover_kg:.2f}.")
