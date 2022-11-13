def take_odd(current_password: str):
    current_password = ''.join([current_password[i] for i in range(len(current_password)) if i % 2 == 1])
    print(current_password)
    return current_password


def cut(current_password: str, index: int, length: int):
    substring = current_password[index:index + length]
    first_part = current_password[:index]
    second_part = current_password[index + length:]
    current_password = first_part + second_part
    print(current_password)
    return current_password


def substitute(current_password: str, substring: str, substitute: str):
    if substring in current_password:
        current_password = current_password.replace(substring, substitute)
        print(current_password)
    else:
        print(f"Nothing to replace!")
    return current_password


password = input()

command = input()

while command != "Done":
    command = command.split()
    if command[0] == "TakeOdd":
        password = take_odd(password)
    elif command[0] == "Cut":
        password = cut(password, int(command[1]), int(command[2]))
    elif command[0] == "Substitute":
        password = substitute(password, command[1], command[2])
    command = input()
print(f"Your password is: {password}")