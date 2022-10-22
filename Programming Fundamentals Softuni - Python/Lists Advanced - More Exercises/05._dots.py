rows = int(input())
board = []
counter = 0
for row in range(rows):
    elements = input().split()
    board.append(elements)

print(*board, sep='\n')

positions_of_dots = []
for row in range(len(board)):
    for col in range(len(board[row])):
        if board[row][col] == '.':
            position = [row, col]
            positions_of_dots.append(position)
connected_dots = 0
dots_rows = []
dots_col = []
for rows in positions_of_dots:
    dots_rows += str(rows[0])
    dots_col += str(rows[1])
dots_rows = [int(i) for i in dots_rows]
dots_col = [int(i) for i in dots_col]
connected_dots = 0
result = []
for dot in range(len(positions_of_dots)):
    current_dot = positions_of_dots[dot]
    next_dot = positions_of_dots[dot + 1]
    if current_dot[0] == next_dot[0]:
        connected_dots += 1
    elif current_dot[1] == next_dot[1]:
        connected_dots += 1
    elif current_dot[0] + next_dot[0] - current_dot[0] > 1:
        result.append(current_dot)
        current_dot = 0
print(result)