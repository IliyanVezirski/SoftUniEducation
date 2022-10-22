number_of_rows = int(input())
ships = []
ships_down = 0
for row in range(number_of_rows):
    ship = input().split()
    ships.append([int(i) for i in ship])

attack = [str(i) for i in input().split()]
for n in attack:
    damage = [int(i) for i in n.split('-')]
    if ships[damage[0]][damage[1]] != 0:
        ships[damage[0]][damage[1]] -= 1
        if ships[damage[0]][damage[1]] == 0:
            ships_down += 1

print(ships_down)