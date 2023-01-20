def read_matrix(row: int):
    matrix = [input().split(', ') for r in range(row)]
    return matrix


matrix = read_matrix(int(input()))
primary = [matrix[r][r] for r in range(len(matrix))]
secondary = [matrix[r][len(matrix) - 1 - r] for r in range(len(matrix))]
print(f"Primary diagonal: {', '.join(primary)}. Sum: {sum(list(map(int, primary)))}")
print(f"Secondary diagonal: {', '.join(secondary)}. Sum: {sum(list(map(int,secondary)))}")
