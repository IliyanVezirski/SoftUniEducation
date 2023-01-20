start_point = ord('a')

raws, col = [int(i) for i in input().split()]
matrix = []
[matrix.append([(f"{chr(start_point + r)}{chr(start_point + r + c)}{chr(start_point + r)}") for c in range(col)]) for r
 in
 range(raws)]
[print(*matrix[r], sep=' ') for r in range(len(matrix))]
