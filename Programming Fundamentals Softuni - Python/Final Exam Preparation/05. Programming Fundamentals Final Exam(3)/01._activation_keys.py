def contains(current_string: str, string_to_check):
    if string_to_check in current_string:
        print(f"{current_string} contains {string_to_check}")
    else:
        print(f"Substring not found!")
    return current_string


def flip(current_string: str, command: str, start_index: int, end_index: int):
    if command == "Upper":
        current_string = current_string[:start_index] + current_string[start_index:end_index].upper() + current_string[
                                                                                                        end_index:]
    else:
        current_string = current_string[:start_index] + current_string[start_index:end_index].lower() + current_string[
                                                                                                        end_index:]
    print(current_string)
    return current_string


def slice(current_string: str, start_index: int, end_index: int):
    current_string = current_string[:start_index] + current_string[end_index:]
    print(current_string)
    return current_string


string = input()

command = input()

while command != "Generate":
    command = command.split(">>>")
    if command[0] == "Flip":
        string = flip(string, command[1], int(command[2]), int(command[3]))
    elif command[0] == "Contains":
        string = contains(string, command[1])
    elif command[0] == "Slice":
        string = slice(string, int(command[1]), int(command[2]))
    command = input()
print(f"Your activation key is: {string}")
