gradus = int(input())
time = input()
outfit = ''
shoes = ''
if time == 'Morning':
    if 10 <= gradus <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < gradus <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif gradus >= 25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif time == 'Afternoon':
    if 10 <= gradus <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < gradus <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif gradus >= 25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
elif time == 'Evening':
    if 10 <= gradus <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < gradus <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif gradus >= 25:
        outfit = 'Shirt'
        shoes = 'Moccasins'
print("It's "+ str(gradus) + " degrees, get your " + outfit + " and " + shoes + ".")
