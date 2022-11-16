def if_contain(current_key: str, substring: str):
    if substring in current_key:
        print(f"{current_key} contains {substring}")
    else:
        print(f"Substring not found!")
    return current_key


def flip_upper_lower(current_key: str, command: str, start_index: int, end_index: int):
    string_to_flip = current_key[start_index:end_index]
    if command == "Lower":
        string_to_flip = string_to_flip.lower()
    else:
        string_to_flip = string_to_flip.upper()
    first_part = current_key[:start_index]
    second_part = current_key[end_index:]
    current_key = first_part + string_to_flip + second_part
    print(current_key)
    return current_key


def slice(current_key: str, start_index: int, end_index: int):
    first_part = current_key[:start_index]
    second_part = current_key[end_index:]
    current_key = first_part + second_part
    print(current_key)
    return current_key


key = input()

command = input()

while command != "Generate":
    command = command.split(">>>")
    if command[0] == "Contains":
        key = if_contain(key, command[1])
    elif command[0] == "Flip":
        key = flip_upper_lower(key, command[1], int(command[2]), int(command[3]))
    elif command[0] == "Slice":
        key = slice(key, int(command[1]), int(command[2]))
    command = input()
print(f"Your activation key is: {key}")
