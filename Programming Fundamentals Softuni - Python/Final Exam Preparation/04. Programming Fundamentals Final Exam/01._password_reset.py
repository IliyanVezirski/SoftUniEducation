"""
Yet again, you have forgotten your password. Naturally, it's not the first time this has happened. Actually, you got so
tired of it that you decided to help yourself with an intelligent solution.
Write a password reset program that performs a series of commands upon a predefined string. First, you will receive a string,
 and afterward, until the command "Done" is given, you will be receiving strings with commands split by a single space.
 The commands will be the following:
•	"TakeOdd"
o	 Takes only the characters at odd indices and concatenates them to obtain the new raw password and then prints it.
•	"Cut {index} {length}"
o	Gets the substring with the given length starting from the given index from the password and removes its first occurrence,
then prints the password on the console.
o	The given index and the length will always be valid.
•	"Substitute {substring} {substitute}"
o	If the raw password contains the given substring, replaces all of its occurrences with the substitute text given and
 prints the result.
o	If it doesn't, prints "Nothing to replace!".
Input
•	You will be receiving strings until the "Done" command is given.
Output
•	After the "Done" command is received, print:
o	"Your password is: {password}"
Constraints
•	The indexes from the "Cut {index} {length}" command will always be valid.

"""
password = input()


def take(string: str):
    new_password = ''
    for i in range(len(string)):
        if i % 2 == 1:
            new_password += string[i]
    print(new_password)
    return new_password


def cut(string: str, start_point: int, length_to_cut: int):
    part_one = string[:start_point]
    part_two = string[start_point+length_to_cut:]
    string = part_one + part_two
    print(string)
    return string


def substitute(string: str, substring: str, substitute: str):
    if substring not in string:
        print("Nothing to replace!")
    else:
        string = string.replace(substring, substitute)
        print(string)
    return string


data = input()

while data != "Done":
    data = data.split()
    if data[0] == "TakeOdd":
        password = take(password)
    elif data[0] == "Cut":
        password = cut(password, int(data[1]), int(data[2]))
    elif data[0] == "Substitute":
        password = substitute(password, data[1], data[2])
    data = input()

print(f"Your password is: {password}")
