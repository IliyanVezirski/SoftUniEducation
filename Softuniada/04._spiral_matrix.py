def right_direction(matrix: list):
    for col_index in range(len(matrix[0])):
        spiral_matrix.append(matrix[0][col_index])
    matrix.pop(0)


def down_direction(matrix: list):
    for row_index in range(len(matrix)):
        spiral_matrix.append(matrix[row_index][-1])
        matrix[row_index].pop(-1)


def left_direction(matrix: list):
    for col_index in range(len(matrix[-1]) - 1, -1, -1):
        spiral_matrix.append(matrix[-1][col_index])
    matrix.pop(-1)


def up_direction(matrix: list):
    for row_index in range(len(matrix) - 1, -1, -1):
        spiral_matrix.append(matrix[row_index][0])
    for row_index in range(len(matrix)):
        matrix[row_index].pop(0)


rows = int(input())
cols = int(input())
matrix = [input().split() for row in range(rows)]
spiral_matrix = []
while matrix:
    if matrix:
        right_direction(matrix)
    if matrix:
        down_direction(matrix)

    if matrix:
        left_direction(matrix)

    if matrix:
        up_direction(matrix)
print(' '.join(spiral_matrix))
