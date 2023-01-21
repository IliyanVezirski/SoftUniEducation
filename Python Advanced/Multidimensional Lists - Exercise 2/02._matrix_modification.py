matrix_size = int(input())
matrix = [[int(i) for i in input().split()] for r in range(matrix_size)]

command = input()
while command != "END":
    current_commnad, *data = command.split()
    data = [int(i) for i in data]
    if current_commnad == "Add":
        if data[0] in range(matrix_size) and data[1] in range(matrix_size):
            matrix[data[0]][data[1]] += data[2]
        else:
            print(f"Invalid coordinates")
    elif current_commnad == "Subtract":
        if data[0] in range(matrix_size) and data[1] in range(matrix_size):
            matrix[data[0]][data[1]] -= data[2]
        else:
            print(f'Invalid coordinates')
    command = input()
[print(' '.join([str(i) for i in r])) for r in matrix]