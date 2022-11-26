def add_stop(current_string: str, index_to_input: int, string_to_input: str):
    current_string = current_string[:index_to_input] + string_to_input + current_string[index_to_input:]
    print(current_string)
    return current_string


def remove_stop(current_string: str, start_index: int, end_index: int):
    if start_index in range(len(current_string)) and end_index in range(len(current_string)):
        current_string = current_string[:start_index] + current_string[end_index+1:]
    print(current_string)
    return current_string


def change_string(current_string: str, old_string: str, new_string: str):
    current_string = current_string.replace(old_string, new_string)
    print(current_string)
    return current_string


string = input()

command = input()
while command != "Travel":
    command = command.split(":")
    if command[0] == "Add Stop":
        string = add_stop(string, int(command[1]), command[2])
    elif command[0] == "Remove Stop":
        string = remove_stop(string, int(command[1]), int(command[2]))
    elif command[0] == "Switch":
        string = change_string(string, command[1], command[2])
    command = input()
print(f"Ready for world tour! Planned stops: {string}")
