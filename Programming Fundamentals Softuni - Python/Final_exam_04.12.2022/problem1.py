def translate(current_string: str, old_string: str, new_string: str):
    current_string = current_string.replace(old_string, new_string)
    print(current_string)
    return current_string


def includes(current_string: str, string_to_check: str):
    if string_to_check in current_string:
        return True
    return False


def start(current_string: str, string_to_check: str):
    if current_string.startswith(string_to_check):
        return True
    return False


def lowercase(current_string: str):
    current_string = current_string.lower()
    print(current_string)
    return current_string


def find_index(current_string: str, char_to_find: str):
    for index in range(len(current_string) - 1, -1, -1):
        if current_string[index] == char_to_find:
            print(index)
            break
    return current_string


def remove_index(current_string: str, start_index: int, count_to_remove: int):
    current_string = current_string[:start_index] + current_string[start_index + count_to_remove:]
    print(current_string)
    return current_string


string = input()

command = input()

while command != "End":
    command = command.split()
    current_command = command[0]
    if current_command == "Translate":
        string = translate(string, command[1], command[2])
    elif current_command == "Includes":
        print(includes(string, command[1]))
    elif current_command == "Start":
        print(start(string, command[1]))
    elif current_command == "Lowercase":
        string = lowercase(string)
    elif current_command == "FindIndex":
        find_index(string, command[1])
    elif current_command == "Remove":
        string = remove_index(string, int(command[1]), int(command[2]))
    command = input()
