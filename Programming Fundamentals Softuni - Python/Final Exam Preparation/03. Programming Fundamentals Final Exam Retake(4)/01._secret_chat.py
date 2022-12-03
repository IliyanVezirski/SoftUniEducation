def insert_space(current_message: str, index: int):
    current_message = current_message[:index] + " " + current_message[index:]
    print(current_message)
    return current_message


def reverse(current_message: str, string_to_reverse: str):
    if string_to_reverse in current_message:
        current_message = current_message.replace(string_to_reverse, '', 1)
        current_message = current_message + string_to_reverse[::-1]
        print(current_message)
    else:
        print(f'error')
    return current_message


def change_all(current_message: str, old_string: str, new_string: str):
    current_message = current_message.replace(old_string, new_string)
    print(current_message)
    return current_message


message = input()

command = input()
while command != "Reveal":
    command = command.split(":|:")
    if command[0] == "ChangeAll":
        message = change_all(message, command[1], command[2])
    elif command[0] == "Reverse":
        message = reverse(message, command[1])
    elif command[0] == "InsertSpace":
        message = insert_space(message, int(command[1]))
    command = input()

print(f'You have a new text message: {message}')
