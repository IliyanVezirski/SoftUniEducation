import textwrap

string = input().split()


def merge(strings: list, start_index: int, end_index: int):
    if start_index not in range(len(strings)):
        strings[:end_index] = [''.join(strings[:end_index])]
    elif end_index not in range(len(strings)):
        strings[start_index:] = [''.join(strings[start_index:])]
    else:
        strings[start_index:end_index] = [''.join(strings[start_index:end_index + 1])]
    return strings


def divide(strings: list, index: int, split: int):
    new_word = strings[index]
    new_list = ''
    cicle = len(new_word) // split

    for i in range(0, len(new_word), cicle):
        word_to_append = new_word[i: cicle + i]
        new_list += ' ' + word_to_append
    strings[index] = new_list
    if len(new_list) != strings[index]:
        strings[index][-1] = new_list[-1]
    strings = [word for line in strings for word in line.split()]


    return strings


command = input()

while command != "3:1":
    command = command.split()
    if command[0] == "merge":
        merge(string, int(command[1]), int(command[2]))
    elif command[0] == "divide":
        divide(string, int(command[1]), int(command[2]))
    command = input()

print(*string)
