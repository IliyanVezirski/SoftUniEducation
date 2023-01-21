matrix_size = int(input())

matrix = [input().split() for r in range(matrix_size)]

bunny_position = tuple()
for r in range(matrix_size):
    for c in range(matrix_size):
        if matrix[r][c] == "B":
            bunny_position = (r, c)
directions = {
    'right': [],
    'left': [],
    'down': [],
    'up': []

}
directions_sums = {
    'right': 0,
    'left': 0,
    'down': 0,
    'up': 0
}
for left in range(bunny_position[1] - 1, -1, -1):
    if matrix[bunny_position[0]][left].isdigit():
        directions['left'].append([bunny_position[0], left])
        directions_sums['left'] += int(matrix[bunny_position[0]][left])
    elif matrix[bunny_position[0]][left] == "X":
        break
for right in range(bunny_position[1], matrix_size):
    if matrix[bunny_position[0]][right].isdigit():
        directions['right'].append((bunny_position[0], right))
        directions_sums['right'] += int(matrix[bunny_position[0]][right])
    elif matrix[bunny_position[0]][right] == "X":
        break
for down in range(bunny_position[0], matrix_size):
    if matrix[down][bunny_position[1]].isdigit():
        directions['down'].append((down,bunny_position[1]))
        directions_sums['down'] += int(matrix[down][bunny_position[1]])
    elif matrix[down][bunny_position[1]] == "X":
        break
for up in range(bunny_position[0] -1, -1, -1):
    if matrix[up][bunny_position[1]].isdigit():
        directions['up'].append((up,bunny_position[1]))
        directions_sums['up'] += int(matrix[up][bunny_position[1]])
    elif matrix[up][bunny_position[1]] == "X":
        break
best_direction = -9999999999
best_direction_name = ''
for direction, current_sum in directions_sums.items():
    if current_sum > best_direction:
        best_direction_name = direction
        best_direction = current_sum
print(best_direction_name)
for direction, positions in directions.items():
    if direction == best_direction_name:
        for position in positions:
            print(f"[{position[0]}, {position[1]}]")
print(best_direction)