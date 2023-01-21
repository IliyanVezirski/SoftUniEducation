raws, col = [int(i) for i in input().split(', ')]

matrix = [[int(i) for i in input().split(', ')] for r in range(raws)]
biggest_sum = 0
biggest_matrix = []
for r in range(raws - 1):
    for c in range(col - 1):
        current_sum = 0
        current_sum += matrix[r][c]
        current_sum += matrix[r + 1][c]
        current_sum += matrix[r + 1][c + 1]
        current_sum += matrix[r][c + 1]
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            biggest_matrix = []
            biggest_matrix.append([matrix[r][c], matrix[r][c + 1]])
            biggest_matrix.append([matrix[r + 1][c], matrix[r + 1][c + 1]])

for r in range(len(biggest_matrix)):
    for c in range(len(biggest_matrix[r])):
        print(biggest_matrix[r][c], end=' ')
    print()
print(biggest_sum)