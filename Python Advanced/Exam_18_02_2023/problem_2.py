rows, col = [int(i) for i in input().split()]
my_position = tuple()
oponent_hit = 0
movement = 0


def check_if_in_field(rows, col, position):
    if position[0] in range(rows) and position[1] in range(col):
        return True
    return False


directions = {
    'left': (0, -1),
    'right': (0, +1),
    'up': (-1, 0),
    'down': (+1, 0)
}
field = []
for row in range(rows):
    field.append(input().split())
    if "B" in field[row]:
        my_position = (row, field[row].index('B'))

command = input()
while command != "Finish":
    new_position = (directions[command][0] + my_position[0], directions[command][1] + my_position[1])
    if check_if_in_field(rows, col, new_position):
        if field[new_position[0]][new_position[1]] == "O":
            new_position = my_position
        elif field[new_position[0]][new_position[1]] == "P":
            field[new_position[0]][new_position[1]] = 'B'
            field[my_position[0]][my_position[1]] = '-'
            movement += 1
            oponent_hit += 1
        else:
            field[my_position[0]][my_position[1]] = '-'
            field[new_position[0]][new_position[1]] = 'B'
            movement += 1
        if oponent_hit == 3:
            break
        my_position = new_position
    command = input()
print(f'Game over!')
print(f'Touched opponents: {oponent_hit} Moves made: {movement}')
