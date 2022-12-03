def move_letter(current_string: str, number_of_letters_to_move: int):
    string_to_move = current_string[:number_of_letters_to_move]
    current_string = current_string[number_of_letters_to_move:] + string_to_move
    return current_string


def insert(current_string: str, index: int, value: str):
    current_string = current_string[:index] + value + current_string[index:]
    return current_string


def change_all(current_string: str, old_value: str, new_value: str):
    current_string = current_string.replace(old_value, new_value)
    return current_string


string = input()

command = input()

while command != "Decode":
    command = command.split("|")
    if command[0] == "Move":
        string = move_letter(string, int(command[1]))
    elif command[0] == "Insert":
        string = insert(string, int(command[1]), command[2])
    elif command[0] == "ChangeAll":
        string = change_all(string, command[1], command[2])
    command = input()
print(f"The decrypted message is: {string}")
