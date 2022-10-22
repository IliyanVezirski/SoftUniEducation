maze = []
rows = int(input())
position = []
found_position = False

left_position = []
right_position = []
down_position = []
up_position = []
for index in range(rows):
    row = [i for i in input()]
    maze.append(row)

for row in range(len(maze)):
    if found_position:
        break
    for col in range(len(maze[row])):
        if maze[row][col] == 'k':
            position = [row, col]
            found_position = True
            break

move = 0


def left(position: list):
    position_to_check = position.copy()
    position_to_check[1] -= 1
    return position_to_check


def right(position: list):
    position_to_check = position.copy()
    position_to_check[1] += 1
    return position_to_check


def up(position: list):
    position_to_check = position.copy()
    position_to_check[0] -= 1
    return position_to_check


def down(position: list):
    position_to_check = position.copy()
    position_to_check[0] += 1
    return position_to_check


while True:
    left_position = left(position)
    right_position = right(position)
    down_position = down(position)
    up_position = up(position)
    if left_position[1] >= len(maze[0]):
        print(f'Kate got out in {move + 1} moves')
        break
    elif right_position[1] >= len(maze[0]):
        print(f'Kate got out in {move + 1} moves')
        break
    elif down_position[0] >= len(maze):
        print(f'Kate got out in {move + 1} moves')
        break
    elif up_position[0] >= len(maze):
        print(f'Kate got out in {move + 1} moves')
        break
    if maze[left_position[0]][left_position[1]] != '#':
        old_position = position.copy()
        position = left(position)
        move += 1
        maze[old_position[0]][old_position[1]] = '#'
        maze[position[0]][position[1]] = 'k'
    elif maze[right_position[0]][right_position[1]] != "#":
        old_position = position.copy()
        position = right(position)
        move += 1
        maze[old_position[0]][old_position[1]] = "#"
        maze[position[0]][position[1]] = 'k'
    elif maze[down_position[0]][down_position[1]] != "#":
        old_position = position.copy()
        position = down(position)
        move += 1
        maze[old_position[0]][old_position[1]] = '#'
        maze[position[0]][position[1]] = 'k'
    elif maze[up_position[0]][up_position[1]] != '#':
        old_position = position.copy()
        position = up(position)
        move += 1
        maze[old_position[0]][old_position[1]] = "#"
        maze[position[0]][position[1]] = 'k'
    else:
        print(f"Kate cannot get out")
        break
    left_position = []
    right_position = []
    down_position = []
    up_position = []
