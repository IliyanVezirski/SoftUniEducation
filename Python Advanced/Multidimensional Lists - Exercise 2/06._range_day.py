def new_directions(direction, current_position: tuple, steps=1):
    if direction == "right":
        return current_position[0], current_position[1] + steps
    elif direction == "left":
        return current_position[0], current_position[1] - steps
    elif direction == 'down':
        return current_position[0] + steps, current_position[1]
    elif direction == 'up':
        return current_position[0] - steps, current_position[1]


def is_in_matrix(position: tuple, size=5):
    if position[0] in range(size) and position[1] in range(size):
        return True
    return False


matrix_size = 5
matrix = []
left_targets = 0
position_of_shooter = tuple()
targets = []

for r in range(matrix_size):
    current_raw = input().split()
    for c in range(len(current_raw)):
        if current_raw[c] == "A":
            position_of_shooter = (r, c)
        elif current_raw[c] == "x":
            left_targets += 1
    matrix.append(current_raw)
matrix[position_of_shooter[0]][position_of_shooter[1]] = '.'
for _ in range(int(input())):
    command = input().split()
    current_command = command[0]
    direction = command[1]
    if current_command == "move":
        steps = int(command[2])
        if is_in_matrix(new_directions(direction, position_of_shooter, steps)):
            new_position = new_directions(direction, position_of_shooter, steps)
            if matrix[new_position[0]][new_position[1]] == '.':
                position_of_shooter = new_position
    else:
        new_position = new_directions(direction, position_of_shooter)
        while is_in_matrix(new_position):
            if matrix[new_position[0]][new_position[1]] == 'x':
                left_targets -= 1
                targets.append([new_position[0], new_position[1]])
                matrix[new_position[0]][new_position[1]] = '.'
                break
            new_position = new_directions(direction, new_position)
    if left_targets == 0:
        break
if left_targets == 0:
    print(f'Training completed! All {len(targets)} targets hit.')
else:
    print(f'Training not completed! {left_targets} targets left.')
if targets:
    print(*targets, sep='\n')
