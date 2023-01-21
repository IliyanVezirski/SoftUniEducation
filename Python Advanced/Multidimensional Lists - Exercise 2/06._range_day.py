matrix_size = 5
field = [input().split() for r in range(matrix_size)]
position = tuple()
shots_positions = []
for r in range(matrix_size):
    for c in range(matrix_size):
        if field[r][c] == "A":
            position = (r, c)
number_of_commands = int(input())
for _ in range(number_of_commands):
    command = input().split()
    if command[0] == "move":
        if command[1] == "up":
            new_position = (position[0] - int(command[2]), position[1])
        elif command[1] == "down":
            new_position = (position[0] + int(command[2]), position[1])
        elif command[1] == "left":
            new_position = (position[0], int(command[2]) - position[1])
        elif command[1] == "right":
            new_position = (position[0], int(command[2]) + position[1])
        if new_position[0] in range(5) and new_position[1] in range(5):
            if field[new_position[0]][new_position[1]] == ".":
                field[position[0]][position[1]] = "."
                field[new_position[0]][new_position[1]] = 'A'
                position = new_position
        else:
            continue
    elif command[0] == "shoot":
        if command[1] == 'right':
            for right in range(position[1], 5):
                if field[position[0]][right] == "x":
                    field[position[0]][right] = '.'
                    shots_positions.append([position[0], right])
                    break
        elif command[1] == "left":
            for left in range(position[1] - 1, -1, -1):
                if field[position[0]][left] == "x":
                    field[position[0]][left] = '.'
                    shots_positions.append([position[0], left])
                    break
        elif command[1] == "down":
            for down in range(position[0], 5):
                if field[down][position[1]] == "x":
                    field[down][position[1]] = '.'
                    shots_positions.append([down, position[1]])
                    break
        elif command == "up":
            for up in range(position[0] - 1, -1, -1):
                if field[up][position[1]] == "x":
                    field[up][position[1]] = '.'
                    shots_positions.append([up, position[1]])
                    break
left_targets = 0
for r in range(5):
    for c in range(5):
        if field[r][c] == "x":
            left_targets += 1
if left_targets > 0:
    print(f'Training not completed! {left_targets} targets left.')
    [print(r) for r in shots_positions]
else:
    print(f'Training completed! All {len(shots_positions)} targets hit.')
    [print(r) for r in shots_positions]
