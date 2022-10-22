values = [int(i) for i in input().split()]


def swap(numbers: list, index_1: int, index_2: int):
    numbers[index_1], numbers[index_2] = numbers[index_2], numbers[index_1]
    return numbers


def multiply(numbers: list, index_1: int, multiply_index: int):
    numbers[index_1] *= numbers[multiply_index]
    return numbers


def decrease(numbers: list):
    for i in range(len(numbers)):
        numbers[i] -= 1
    return numbers


command = input()

while command != "end":
    command = command.split()
    if command[0] == "swap":
        swap(values, int(command[1]), int(command[2]))
    elif command[0] == "multiply":
        multiply(values, int(command[1]), int(command[2]))
    elif command[0] == "decrease":
        decrease(values)
    command = input()
print(*values, sep=', ')
