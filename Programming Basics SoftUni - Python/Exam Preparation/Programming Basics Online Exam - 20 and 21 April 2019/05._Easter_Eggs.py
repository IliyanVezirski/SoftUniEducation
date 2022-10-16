painted_eggs = int(input())
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_eggs = 0
max_eggs_colour = 0
for eggs in  range(painted_eggs):
    egg_colour = input()
    if egg_colour == 'red':
        red_eggs += 1
    elif egg_colour == 'orange':
        orange_eggs += 1
    elif egg_colour == 'blue':
        blue_eggs += 1
    elif egg_colour == 'green':
        green_eggs += 1
if red_eggs > max_eggs:
    max_eggs = red_eggs
    max_eggs_colour = 'red'
if blue_eggs > max_eggs:
    max_eggs = blue_eggs
    max_eggs_colour = 'blue'
if orange_eggs > max_eggs:
    max_eggs = orange_eggs
    max_eggs_colour = 'orange'
if green_eggs > max_eggs:
    max_eggs = green_eggs
    max_eggs_colour = 'green'
print(f'Red eggs: {red_eggs}')
print(f'Orange eggs: {orange_eggs}')
print(f'Blue eggs: {blue_eggs}')
print(f'Green eggs: {green_eggs}')
print(f'Max eggs: {max_eggs} -> {max_eggs_colour}')