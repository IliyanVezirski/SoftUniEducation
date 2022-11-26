def take_odd(current_string: str):
    new_string = ''
    for i in range(len(current_string)):
        if i % 2 == 1:
            new_string += current_string[i]
    print(new_string)
    return new_string


def cut(current_string: str, index_to_start: int, length: int):
    string_to_replace = current_string[index_to_start:index_to_start + length]
    current_string = current_string.replace(string_to_replace, '', 1)
    print(current_string)
    return current_string


def substitute(current_string: str, string_to_replace: str, new_string: str):
    if string_to_replace in current_string:
        current_string = current_string.replace(string_to_replace, new_string)
        print(current_string)
    else:
        print(f'Nothing to replace!')
    return current_string


string = input()

command = input()
while command != "Done":
    command = command.split()
    if command[0] == "TakeOdd":
        string = take_odd(string)
    elif command[0] == "Cut":
        string = cut(string, int(command[1]), int(command[2]))
    elif command[0] == "Substitute":
        string = substitute(string, command[1], command[2])

    command = input()

print(f'Your password is: {string}')
