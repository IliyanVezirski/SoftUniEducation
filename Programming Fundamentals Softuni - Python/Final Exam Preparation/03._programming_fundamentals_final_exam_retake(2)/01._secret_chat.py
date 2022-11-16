def insert_space(current_msg: str, index: int):
    first_str = current_msg[:index]
    second_str = current_msg[index:]
    current_msg = first_str + " " + second_str
    print(current_msg)
    return current_msg


def reverse(current_msg: str, substring: str):
    if substring in current_msg:
        current_msg = current_msg.replace(substring, "")
        substring = substring[::-1]
        current_msg = current_msg + substring
        print(current_msg)
        return current_msg
    else:
        print('error')
        return current_msg


def change_all(current_msg: str, substring: str, replacement: str):
    current_msg = current_msg.replace(substring, replacement)
    print(current_msg)
    return current_msg


message = input()

command = input()

while command != "Reveal":
    command = command.split(":|:")
    if command[0] == "InsertSpace":
        message = insert_space(message, int(command[1]))
    elif command[0] == "Reverse":
        message = reverse(message, command[1])
    elif command[0] == "ChangeAll":
        message = change_all(message, command[1], command[2])
    command = input()
print(f"You have a new text message: {message}")
