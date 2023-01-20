raws, col = [int(i) for i in input().split()]
matrix = [input().split() for r in range(raws)]

while True:
    command = input().split()
    if command[0] == "END":
        break
    current_command = command[0]
    data = [int(i) for i in command[1:] if i.isdigit()]
    if data[0] in range(raws) and data[2] in range(raws) and data[1] in range(col) and data[3] in range(col) and len(
            data) == 4:
        matrix[data[0]][data[1]], matrix[data[2]][data[3]] = matrix[data[2]][data[3]], matrix[data[0]][data[1]]
        [print(' '.join(list(map(str, matrix[r])))) for r in range(len(matrix))]
    else:
        print(f'Invalid input!')
