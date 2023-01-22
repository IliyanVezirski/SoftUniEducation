def is_in_matrix(position: tuple, size: int):
    if position[0] in range(size) and position[1] in range(size):
        return True
    else:
        return False


def santa_moves(current_position: tuple, direction):
    if direction == 'left':
        return current_position[0], current_position[1] - 1
    elif direction == 'right':
        return current_position[0], current_position[1] + 1
    elif direction == 'down':
        return current_position[0] + 1, current_position[1]
    elif direction == "up":
        return current_position[0] - 1, current_position[1]


def santa_stop_on_cookie(current_position: tuple, presents_left, nice_kids):
    around_kids = [
        (0, -1),
        (0, +1),
        (+1, 0),
        (-1, 0),
    ]
    for position in around_kids:
        position_to_check = (position[0] + current_position[0], position[1] + current_position[1])
        if is_in_matrix(position_to_check, size_of_neighborhood):
            if neighborhood[position_to_check[0]][position_to_check[1]] in "XV":
                presents_left -= 1
                if neighborhood[position_to_check[0]][position_to_check[1]] == 'V':
                    nice_kids -= 1
            neighborhood[position_to_check[0]][position_to_check[1]] = '-'
    return presents_left, nice_kids


number_of_presents = int(input())
size_of_neighborhood = int(input())
neighborhood = []
santa_position = ()
naughty_kids_places = []
nice_kids_places = []
cookies_places = []

for r in range(size_of_neighborhood):
    neighborhood.append(input().split())
    for c in range(size_of_neighborhood):
        if neighborhood[r][c] == "S":
            santa_position = (r, c)
        elif neighborhood[r][c] == 'X':
            naughty_kids_places.append((r, c))
        elif neighborhood[r][c] == "V":
            nice_kids_places.append((r, c))
        elif neighborhood[r][c] == "C":
            cookies_places.append((r, c))
nice_kids_left = len(nice_kids_places)
command = input()
while command != "Christmas morning":
    new_position = santa_moves(santa_position, command)
    if is_in_matrix(new_position, size_of_neighborhood):
        if neighborhood[new_position[0]][new_position[1]] == "C":
            neighborhood[santa_position[0]][santa_position[1]] = '-'
            neighborhood[new_position[0]][new_position[1]] = 'S'
            santa_position = new_position
            number_of_presents, nice_kids_left = santa_stop_on_cookie(new_position, number_of_presents, nice_kids_left)
        elif neighborhood[new_position[0]][new_position[1]] == "X":
            neighborhood[santa_position[0]][santa_position[1]] = '-'
            neighborhood[new_position[0]][new_position[1]] = 'S'
            santa_position = new_position
        elif neighborhood[new_position[0]][new_position[1]] == "V":
            neighborhood[santa_position[0]][santa_position[1]] = '-'
            neighborhood[new_position[0]][new_position[1]] = 'S'
            santa_position = new_position
            number_of_presents -= 1
            nice_kids_left -= 1
        else:
            neighborhood[santa_position[0]][santa_position[1]] = '-'
            neighborhood[new_position[0]][new_position[1]] = 'S'
            santa_position = new_position
    if number_of_presents <= 0:
        break
    command = input()
if number_of_presents <= 0 and nice_kids_left > 0:
    print(f'Santa ran out of presents!')
[print(*r) for r in neighborhood]
if nice_kids_left == 0:
    print(f"Good job, Santa! {len(nice_kids_places)} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_left} nice kid/s.")
