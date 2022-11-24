matrix = []
matrix_rows = int(input())
for row in range(matrix_rows):
    matrix.append(list(map(int, input().split())))

attack_moves = input().split()
destroyed_ships = 0
for attack in attack_moves:
    row, col = list(map(int,attack.split("-")))
    if matrix[row][col] != 0:
        matrix[row][col] -= 1
        if matrix[row][col] == 0:
            destroyed_ships += 1
print(destroyed_ships)
