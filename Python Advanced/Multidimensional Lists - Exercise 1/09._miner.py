matrix_size = int(input())
commands = [i for i in input().split()]
position_of_miner = tuple()
matrix = [[i for i in input().split()] for r in range(matrix_size)]
coals_positions = []
for r in range(matrix_size):
    for c in range(matrix_size):
        if matrix[r][c] == "s":
            position_of_miner = (r, c)
        if matrix[r][c] == "c":
            coals_positions.append((r, c))
number_of_coals = len(coals_positions)
coals_collected = 0
lost = False
for current_command in commands:
    if current_command == "up":
        new_position = (position_of_miner[0] - 1, position_of_miner[1])
        if new_position[0] not in range(len(matrix)) or new_position[1] not in range(len(matrix[0])):
            continue
        if matrix[new_position[0]][new_position[1]] == 'c':
            coals_collected += 1
            matrix[new_position[0]][new_position[1]] = '*'
        elif matrix[new_position[0]][new_position[1]] == "e":
            print(f"Game over! {new_position}")
            lost = True
            break
    elif current_command == "right":
        new_position = (position_of_miner[0], position_of_miner[1] + 1)
        if new_position[0] not in range(len(matrix)) or new_position[1] not in range(len(matrix[0])):
            continue
        if matrix[new_position[0]][new_position[1]] == 'c':
            coals_collected += 1
            matrix[new_position[0]][new_position[1]] = '*'
        elif matrix[new_position[0]][new_position[1]] == "e":
            print(f"Game over! {new_position}")
            lost = True
            break
    elif current_command == "left":
        new_position = (position_of_miner[0], position_of_miner[1] - 1)
        if new_position[0] not in range(len(matrix)) or new_position[1] not in range(len(matrix[0])):
            continue
        if matrix[new_position[0]][new_position[1]] == 'c':
            coals_collected += 1
            matrix[new_position[0]][new_position[1]] = '*'
        elif matrix[new_position[0]][new_position[1]] == "e":
            print(f"Game over! {new_position}")
            lost = True
            break
    elif current_command == "down":
        new_position = (position_of_miner[0] + 1, position_of_miner[1])
        if new_position[0] not in range(len(matrix)) or new_position[1] not in range(len(matrix[0])):
            continue
        if matrix[new_position[0]][new_position[1]] == 'c':
            coals_collected += 1
            matrix[new_position[0]][new_position[1]] = '*'
        elif matrix[new_position[0]][new_position[1]] == "e":
            print(f"Game over! {new_position}")
            lost = True
            break
    matrix[position_of_miner[0]][position_of_miner[1]] = '*'
    matrix[new_position[0]][new_position[1]] = 's'
    position_of_miner = new_position
if coals_collected == len(coals_positions) and not lost:
    print(f'You collected all coal! {position_of_miner}')
elif coals_collected != (len(coals_positions)) and not lost:
    print(f'{len(coals_positions) - coals_collected} pieces of coal left. {position_of_miner}')
