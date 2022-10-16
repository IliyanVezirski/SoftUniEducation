level_of_fire = input().split('#')
amount_of_water = int(input())
total_fire = 0
effort = 0
cells = []
for fires in level_of_fire:
    fires = fires.split(' = ')
    level = fires[1]
    if amount_of_water <= 77:
        break
    level = int(level)
    if fires[0] == "High" and level >= 81 and level <= 125:
        amount_of_water -= level
        total_fire += level
        effort += level * 0.25
        cells.append(str(level))
    elif fires[0] == "Medium" and level >= 51 and level <= 80:
        amount_of_water -= level
        total_fire += level
        effort += level * 0.25
        cells.append(str(level))
    elif fires[0] == "Low" and level >= 1 and level <= 50:
        amount_of_water -= level
        total_fire += level
        effort += level * 0.25
        cells.append(str(level))
print('Cells:\n - ' + '\n - '.join(cells))
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')