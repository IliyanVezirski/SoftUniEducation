def read_matrix():
    raw, col = [int(i) for i in input().split()]
    matrix = [input().split() for r in range(raw)]
    return matrix


matrix = read_matrix()
counter = 0
for raw in range(len(matrix) - 1):
    for col in range(len(matrix[0]) - 1):
        if matrix[raw][col] == matrix[raw][col + 1] and matrix[raw + 1][col] == matrix[raw][col] and matrix[raw + 1][
            col + 1] == matrix[raw][col]:
            counter += 1

print(counter)
