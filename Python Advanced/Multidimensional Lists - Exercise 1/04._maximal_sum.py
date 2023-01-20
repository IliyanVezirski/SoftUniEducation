def read_matrix():
    raw, col = [int(i) for i in input().split()]
    matrix = [list(map(int, input().split())) for r in range(raw)]
    return matrix


matrix = read_matrix()
current_sum = float("-inf")
biggest_matrix = []
for raw in range(len(matrix) - 2):
    for col in range(len(matrix[0]) - 2):
        sum_for_current_matrix = sum(matrix[raw][col:col + 3])
        sum_for_current_matrix += sum(matrix[raw + 1][col:col + 3])
        sum_for_current_matrix += sum(matrix[raw + 2][col:col + 3])
        if sum_for_current_matrix > current_sum:
            current_sum = sum_for_current_matrix
            biggest_matrix = []
            biggest_matrix.append(matrix[raw][col:col + 3])
            biggest_matrix.append(matrix[raw + 1][col:col + 3])
            biggest_matrix.append(matrix[raw + 2][col:col + 3])
print(f"Sum = {current_sum}")
[print(' '.join(map(str, r))) for r in biggest_matrix]
