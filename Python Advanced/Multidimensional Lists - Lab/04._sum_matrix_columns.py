raws, col = [int(i) for i in input().split(', ')]

matrix = [[int(i) for i in input().split()] for r in range(raws)]

for c in range(col):
    current_sum = 0
    for r in range(raws):
        current_sum += matrix[r][c]
    print(current_sum)
