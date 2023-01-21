from collections import deque

raws, col = [int(i) for i in input().split()]
word = deque(i for i in input())
matrix = []
for r in range(raws):
    matrix.append([])
    for c in range(col):
        current_letter = word.popleft()
        matrix[r].append(current_letter)
        word.append(current_letter)
for r in range(1, raws + 1):
    if r % 2 == 0:
        matrix[r-1] = list(reversed(matrix[r-1]))

[print(''.join(r))for r in matrix]