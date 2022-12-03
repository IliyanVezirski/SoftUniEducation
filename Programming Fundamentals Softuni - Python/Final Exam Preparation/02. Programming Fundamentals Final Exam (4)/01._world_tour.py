def add(current_string: str, index: int, string_to_input: str):
    if index in range(len(current_string)):
        current_string = current_string[:index] + string_to_input + current_string[index:]
    print(current_string)
    return current_string


def remove(current_string: str, start_index: int, end_index: int):
    if start_index in range(len(current_string)) and end_index in range(len(current_string)):
        current_string = current_string[:start_index] + current_string[end_index + 1:]

    print(current_string)
    return current_string


def switch(current_string: str, old_string: str, new_str: str):
    current_string = current_string.replace(old_string, new_str)
    print(current_string)
    return current_string


string = input()
command = input()

while command != "Travel":
    command = command.split(":")
    if command[0] == "Add Stop":
        string = add(string, int(command[1]), command[2])
    elif command[0] == "Remove Stop":
        string = remove(string, int(command[1]), int(command[2]))
    elif command[0] == "Switch":
        string = switch(string, command[1], command[2])

    command = input()
print(f'Ready for world tour! Planned stops: {string}')
