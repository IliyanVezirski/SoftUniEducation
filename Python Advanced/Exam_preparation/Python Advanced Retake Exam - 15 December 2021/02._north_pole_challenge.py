"""
You are visiting Santa Claus' workshop, and it is complete chaos. You will need to help Santa find all items scattered
around the workshop.
You will be given the size of the matrix in the format "{rows}, {columns}". It is the Santa's workshop represented
 as some symbols separated by a single space:
•	Your position is marked with the symbol "Y"
•	Christmas decorations are marked with the symbol "D"
•	Gifts are marked with the symbol "G"
•	Cookies are marked with the symbol "C"
•	All of the empty positions will be marked with "."
After the field state, you will be given commands until you receive the command "End". The commands will be in the
 format "right/left/up/down-{steps}". You should move in the given direction with the given steps and collect all the
 items that come across. If you go out of the field, you should continue to traverse the field from the opposite side
 in the same direction. You should mark your path with "x". Your current position should always be marked with "Y".
Keep track of all collected items. If you've collected all items at any point, end the program and print: "Merry Christmas!".
Input
•	On the first line, you will receive the number of rows and columns in the format "{rows}, {columns}"
•	On the next lines, you will receive each row with its columns - symbols, separated by a single space.
•	On the following lines, you will receive commands in the format described above until you receive the command "End"
or until you collect all items.
Output
•	On the first line, if you have collected all items, print:
o	"Merry Christmas!"
o	Otherwise, skip the line
•	Next, print the number of collected items in the format:
o	"You've collected:
o	- {number_of_decoration} Christmas decorations
o	- {number_of_gifts} Gifts
o	- {number_of_cookies} Cookies"
•	Finally, print the field, as shown in the examples.
Constrains
•	All the commands will be valid
•	There will always be at least one item
•	The dimensions of the matrix will be integers in the range [1, 20]
•	The field will always have only one "Y"
•	On the field, there will always be only the symbols shown above.

"""

row, col = [int(i) for i in input().split(', ')]
matrix = []
position = tuple()
christmas_decoration = 0
gifts = 0
cookies = 0
items = 0
for r in range(row):
    matrix.append(input().split())
    for c in range(col):
        if matrix[r][c] == "Y":
            position = (r, c)
        if matrix[r][c] == 'D':
            items += 1
        elif matrix[r][c] == 'G':
            items += 1
        elif matrix[r][c] == "C":
            items += 1
command = input()

while command != 'End':
    command = command.split('-')
    step = int(command[1])
    matrix[position[0]][position[1]] = 'x'
    if command[0] == "right":
        current_col = position[1]
        for c in range(0, step):
            current_col += 1
            if current_col == col:
                current_col = 0
            if matrix[position[0]][current_col] == 'D':
                items -= 1
                christmas_decoration += 1
            elif matrix[position[0]][current_col] == 'G':
                items -= 1
                gifts += 1
            elif matrix[position[0]][current_col] == "C":
                items -= 1
                cookies += 1

            current_position = (position[0], current_col)
            matrix[position[0]][current_col] = 'x'
            if items == 0:
                position = (position[0], current_col)
                break
        position = current_position[0], current_position[1]
        matrix[position[0]][position[1]] = 'Y'
    elif command[0] == "left":
        current_col = position[1]
        for c in range(0, step):
            current_col -= 1
            if current_col == -1:
                current_col = col - 1
            if matrix[position[0]][current_col] == 'D':
                items -= 1
                christmas_decoration += 1
            elif matrix[position[0]][current_col] == 'G':
                items -= 1
                gifts += 1
            elif matrix[position[0]][current_col] == "C":
                items -= 1
                cookies += 1

            matrix[position[0]][current_col] = 'x'
            current_position = (position[0], current_col)
            if items == 0:
                position = (position[0], current_col)
                break
        position = current_position[0], current_position[1]
        matrix[position[0]][position[1]] = 'Y'
    elif command[0] == "down":
        current_row = position[0]
        for r in range(0, step):
            current_row += 1
            if current_row == row:
                current_row = 0
            if matrix[current_row][position[1]] == 'D':
                items -= 1
                christmas_decoration += 1
            elif matrix[current_row][position[1]] == 'G':
                items -= 1
                gifts += 1
            elif matrix[current_row][position[1]] == "C":
                items -= 1
                cookies += 1

            matrix[current_row][position[1]] = 'x'
            current_position = (current_row, position[1])
            if items == 0:
                position = (current_row, position[1])
                break
        position = current_position[0], current_position[1]
        matrix[position[0]][position[1]] = 'Y'
    elif command[0] == "up":
        current_row = position[0]
        for r in range(0, step):
            current_row -= 1
            if current_row == -1:
                current_row = row - 1
            if matrix[current_row][position[1]] == 'D':
                items -= 1
                christmas_decoration += 1
            elif matrix[current_row][position[1]] == 'G':
                items -= 1
                gifts += 1
            elif matrix[current_row][position[1]] == "C":
                items -= 1
                cookies += 1
            matrix[current_row][position[1]] = 'x'
            current_position = (current_row, position[1])
            if items == 0:
                position = (current_row, position[1])
                break
        position = current_position[0], current_position[1]
        matrix[position[0]][position[1]] = 'Y'
    if items == 0:
        break
    command = input()
if items == 0:
    print(f'Merry Christmas!')
matrix[position[0]][position[1]] = 'Y'
print(f"You've collected:")
print(f"- {christmas_decoration} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")
[print(' '.join(matrix[r])) for r in range(len(matrix))]

