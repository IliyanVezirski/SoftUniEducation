matrix_size = int(input())

matrix = [[int(i) for i in input().split(', ')] for r in range(matrix_size)]
flat_matrix = []
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        flat_matrix.append(matrix[r][c])
print(flat_matrix)