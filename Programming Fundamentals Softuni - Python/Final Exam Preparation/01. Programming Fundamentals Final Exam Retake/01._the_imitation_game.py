message = input()


def move(string: str, number: int):
    new_string = string[:number]
    string = string[number:] + new_string
    return string


def insert(string: str, index: int, value: str):
    string_list = []
    for i in string:
        string_list.append(i)
    string_list.insert(index, value)
    string = ''.join(string_list)
    return string


def change(string: str, substring: str, replacement: str):
    string = string.replace(substring, replacement)
    return string


command = input()

while command != "Decode":
    command = command.split("|")
    if command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = change(message, substring, replacement)
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        message = insert(message, index, value)
    elif command[0] == "Move":
        number_of_letters = int(command[1])
        message = move(message, number_of_letters)
    command = input()


print(f"The decrypted message is: {message}")