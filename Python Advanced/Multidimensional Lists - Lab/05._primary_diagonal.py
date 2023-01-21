matrix_size = int(input())

matrix = [[int(i) for i in input().split()] for r in range(matrix_size)]

diagonal_sum = 0

for r in range(len(matrix)):
    diagonal_sum += matrix[r][r]
print(diagonal_sum)