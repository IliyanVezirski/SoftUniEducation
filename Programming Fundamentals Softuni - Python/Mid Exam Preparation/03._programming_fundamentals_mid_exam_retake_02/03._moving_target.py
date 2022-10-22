targets = [int(i) for i in input().split()]


def shoot(sequence: list, index: int, damage: int):
    if index in range(len(sequence)):
        sequence[index] -= damage
        if sequence[index] <= 0:
            sequence.pop(index)
    return sequence


def add(sequence: list, index: int, value: int):
    if index in range(len(sequence)):
        sequence.insert(index, value)
    else:
        print(f"Invalid placement!")


def strike(sequence: list, index: int, radius: int):
    start_point = index - radius
    end_point = index + radius
    if start_point in range(len(sequence)) and end_point in range(len(sequence)):
        del sequence[start_point:end_point+1]
    else:
        print(f"Strike missed!")


command = input()

while command != "End":
    command = command.split()
    if command[0] == "Shoot":
        shoot(targets, int(command[1]), int(command[2]))
    elif command[0] == "Add":
        add(targets, int(command[1]), int(command[2]))
    elif command[0] == "Strike":
        strike(targets, int(command[1]), int(command[2]))
    command = input()

print(*targets, sep='|')
