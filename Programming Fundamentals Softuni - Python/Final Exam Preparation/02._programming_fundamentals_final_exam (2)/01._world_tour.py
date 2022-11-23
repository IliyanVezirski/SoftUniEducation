def stop(string: str, index: int, substring: str):
    if index in range(len(string)):
        string = string[:index] + substring + string[index:]
    print(string)
    return string


def remove(string: str, start_index: int, end_index: int):
    if start_index in range(len(string)) and end_index in range(len(string)):
        string = string[:start_index] + string[end_index+1:]
    print(string)
    return string


def switch(string: str, old_string: str, new_string: str):
    if old_string in string:
        string = string.replace(old_string, new_string)
    print(string)
    return string


string = input()
command = input()

while command != "Travel":
    command = command.split(":")
    if command[0] == "Add Stop":
        string = stop(string, int(command[1]), command[2])
    elif command[0] == "Remove Stop":
        string = remove(string, int(command[1]), int(command[2]))
    elif command[0] == "Switch":
        string = switch(string, command[1], command[2])
    command = input()
print(f"Ready for world tour! Planned stops: {string}")
