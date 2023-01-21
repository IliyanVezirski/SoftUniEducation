matrix_size = int(input())

matrix = [[int(i) for i in input().split(', ')] for r in range(matrix_size)]
even_matrix = []

for r in range(matrix_size):
    even_matrix.append([i for i in matrix[r] if i % 2 == 0])
print(even_matrix)
