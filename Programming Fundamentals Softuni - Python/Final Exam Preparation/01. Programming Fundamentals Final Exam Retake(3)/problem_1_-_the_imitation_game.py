def move(current_message: str, number_of_characters: int):
    current_message = current_message[number_of_characters:] + current_message[:number_of_characters]
    return current_message


def insert_value(current_message: str, index_to_input: int, value: str):
    current_message = current_message[:index_to_input] + value + current_message[index_to_input:]
    return current_message


def change_all(current_message: str, old_string: str, new_string: str):
    current_message = current_message.replace(old_string, new_string)
    return current_message


def final_print(current_message: str):
    print(f"The decrypted message is: {current_message}")


secret_message = input()

command = input()

while command != "Decode":
    command = command.split("|")
    if command[0] == "ChangeAll":
        secret_message = change_all(secret_message, command[1], command[2])
    elif command[0] == "Insert":
        secret_message = insert_value(secret_message, int(command[1]), command[2])
    elif command[0] == "Move":
        secret_message = move(secret_message, int(command[1]))
    command = input()

final_print(secret_message)


