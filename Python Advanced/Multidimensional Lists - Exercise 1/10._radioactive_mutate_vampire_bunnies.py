raws, col = [int(i) for i in input().split()]
matrix = []
for raw in range(raws):
    matrix.append([i for i in input()])

player_position = tuple()
for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if matrix[r][c] == "P":
            player_position = (r, c)
commands = [i for i in input()]
player_won = False
player_died = False
bunnies_positions = []
for current_command in commands:
    if current_command == "L":
        new_position = (player_position[0], player_position[1] - 1)
    elif current_command == "R":
        new_position = (player_position[0], player_position[1] + 1)
    elif current_command == "U":
        new_position = (player_position[0] - 1, player_position[1])
    elif current_command == "D":
        new_position = (player_position[0] + 1, player_position[1])
    if new_position[0] not in range(raws) or new_position[1] not in range(col):
        player_won = True
    elif matrix[new_position[0]][new_position[1]] == "B":
        player_died = True
    if not player_won:
        matrix[new_position[0]][new_position[1]] = "P"
    matrix[player_position[0]][player_position[1]] = "."
    positions_of_bunnies = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == "B":
                positions_of_bunnies.append((r, c))
    for position in positions_of_bunnies:
        if position[1] - 1 in range(len(matrix[0])):
            if matrix[position[0]][position[1] - 1] == "P":
                player_died = True
            matrix[position[0]][position[1] - 1] = "B"
        if position[1] + 1 in range(len(matrix[0])):
            if matrix[position[0]][position[1] + 1] == "P":
                player_died = True
            matrix[position[0]][position[1] + 1] = "B"
        if position[0] + 1 in range(len(matrix)):
            if matrix[position[0] + 1][position[1]] == "P":
                player_died = True
            matrix[position[0] + 1][position[1]] = "B"
        if position[0] - 1 in range(len(matrix)):
            if matrix[position[0] - 1][position[1]] == "P":
                player_died = True
            matrix[position[0] - 1][position[1]] = "B"
    if player_won:
        [print(''.join(r)) for r in matrix]
        print(f"won: {player_position[0]} {player_position[1]}")
        break
    if player_died:
        [print(''.join(r)) for r in matrix]
        print(f"dead: {new_position[0]} {new_position[1]}")
        break
    player_position = new_position