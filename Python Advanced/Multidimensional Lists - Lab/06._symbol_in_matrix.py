matrix_size = int(input())
position = tuple()
matrix = [[i for i in input()] for r in range(matrix_size)]
searched_letter = input()

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == searched_letter:
            position = (r, c)
            break

if position:
    print(position)
else:
    print(f"{searched_letter} does not occur in the matrix")
