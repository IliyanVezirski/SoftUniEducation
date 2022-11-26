def insert_space(current_message: str, index_for_whitespace: int):
    current_message = current_message[:index_for_whitespace] + " " + current_message[index_for_whitespace:]
    print(current_message)
    return current_message


def reverse_string(current_message: str, string_to_reverse: str):
    if string_to_reverse not in current_message:
        print(f"error")
    else:
        current_message = current_message.replace(string_to_reverse, '', 1)
        string_to_reverse = string_to_reverse[::-1]
        current_message = current_message + string_to_reverse
        print(current_message)
    return current_message


def change_string(current_message: str, old_string: str, new_str: str):
    current_message = current_message.replace(old_string, new_str)
    print(current_message)
    return current_message


string = input()

command = input()

while command != "Reveal":
    command = command.split(":|:")
    if command[0] == "ChangeAll":
        string = change_string(string, command[1], command[2])
    elif command[0] == "Reverse":
        string = reverse_string(string, command[1])
    elif command[0] == "InsertSpace":
        string = insert_space(string, int(command[1]))
    command = input()
print(f"You have a new text message: {string}")
