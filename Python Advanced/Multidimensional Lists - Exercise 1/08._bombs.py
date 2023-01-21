matrix_size = int(input())

matrix = [[int(i) for i in input().split()] for r in range(matrix_size)]
bombs = [r for r in input().split()]

for current_bomb in bombs:
    current_bomb = tuple(int(i) for i in current_bomb.split(','))
    if matrix[current_bomb[0]][current_bomb[1]] > 0:
        bomb_power = matrix[current_bomb[0]][current_bomb[1]]
        if current_bomb[1] + 1 in range(matrix_size):
            if matrix[current_bomb[0]][current_bomb[1] + 1] > 0:
                matrix[current_bomb[0]][current_bomb[1] + 1] -= bomb_power
        if current_bomb[1] - 1 in range(matrix_size):
            if matrix[current_bomb[0]][current_bomb[1] - 1] > 0:
                matrix[current_bomb[0]][current_bomb[1] - 1] -= bomb_power
        if current_bomb[0] + 1 in range(matrix_size):
            if matrix[current_bomb[0] + 1][current_bomb[1]] > 0:
                matrix[current_bomb[0] + 1][current_bomb[1]] -= bomb_power
        if current_bomb[0] - 1 in range(matrix_size):
            if matrix[current_bomb[0] - 1][current_bomb[1]] > 0:
                matrix[current_bomb[0] - 1][current_bomb[1]] -= bomb_power
        if current_bomb[0] - 1 in range(matrix_size) and current_bomb[1] - 1 in range(matrix_size):
            if matrix[current_bomb[0] - 1][current_bomb[1] - 1] > 0:
                matrix[current_bomb[0] - 1][current_bomb[1] - 1] -= bomb_power
        if current_bomb[0] + 1 in range(matrix_size) and current_bomb[1] + 1 in range(matrix_size):
            if matrix[current_bomb[0] + 1][current_bomb[1] + 1] > 0:
                matrix[current_bomb[0] + 1][current_bomb[1] + 1] -= bomb_power
        if current_bomb[0] + 1 in range(matrix_size) and current_bomb[1] - 1 in range(matrix_size):
            if matrix[current_bomb[0] + 1][current_bomb[1] - 1] > 0:
                matrix[current_bomb[0] + 1][current_bomb[1] - 1] -= bomb_power
        if current_bomb[0] - 1 in range(matrix_size) and current_bomb[1] + 1 in range(matrix_size):
            if matrix[current_bomb[0] - 1][current_bomb[1] + 1] > 0:
                matrix[current_bomb[0] - 1][current_bomb[1] + 1] -= bomb_power
        matrix[current_bomb[0]][current_bomb[1]] = 0
alive_cells = []
for r in range(matrix_size):
    for c in range(matrix_size):
        if matrix[r][c] > 0:
            alive_cells.append(matrix[r][c])
print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
for r in range(matrix_size):
    print(*matrix[r])
