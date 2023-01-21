raws, col = [int(i) for i in input().split(', ')]
matrix = []
sum_of_matrix = 0
for r in range(raws):
    matrix.append([int(i) for i in input().split(', ')])
for r in range(raws):
    for c in range(col):
        sum_of_matrix += matrix[r][c]
print(sum_of_matrix)
print(matrix)
