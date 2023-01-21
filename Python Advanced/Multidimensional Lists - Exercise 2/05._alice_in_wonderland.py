wonderland_size = int(input())
wonderland = [input().split() for r in range(wonderland_size)]

alice_position = tuple()
tea_bags = 0

for r in range(wonderland_size):
    for c in range(wonderland_size):
        if wonderland[r][c] == "A":
            alice_position = (r, c)
while True:
    command = input()
    if command == 'down':
        new_position = (alice_position[0] + 1, alice_position[1])
    elif command == "up":
        new_position = (alice_position[0] - 1, alice_position[1])
    elif command == "right":
        new_position = (alice_position[0], alice_position[1] + 1)
    elif command == "left":
        new_position = (alice_position[0], alice_position[1] - 1)
    if new_position[0] not in range(wonderland_size) or new_position[1] not in range(wonderland_size):
        wonderland[alice_position[0]][alice_position[1]] = '*'
        print(f"Alice didn't make it to the tea party.")
        [print(' '.join(r)) for r in wonderland]
        break
    if wonderland[new_position[0]][new_position[1]] == "R":
        wonderland[alice_position[0]][alice_position[1]] = '*'
        wonderland[new_position[0]][new_position[1]] = '*'
        print(f"Alice didn't make it to the tea party.")
        [print(' '.join(r))for r in wonderland]
        break
    if wonderland[new_position[0]][new_position[1]].isdigit():
        tea_bags += int(wonderland[new_position[0]][new_position[1]])
    wonderland[alice_position[0]][alice_position[1]] = '*'
    if tea_bags >= 10:
        wonderland[new_position[0]][new_position[1]] = '*'
        print(f'She did it! She went to the party.')
        [print(' '.join(r)) for r in wonderland]
        break
    alice_position = new_position
