def read_matrix(raw: int):
    matrix = [input().split() for r in range(raw)]
    return matrix


matrix = read_matrix(int(input()))
primary = [matrix[r][r] for r in range(len(matrix))]
secondary = [matrix[r][len(matrix) - 1 - r] for r in range(len(matrix))]
difference = abs(sum(map(int, primary)) - sum(map(int, secondary)))
print(difference)
