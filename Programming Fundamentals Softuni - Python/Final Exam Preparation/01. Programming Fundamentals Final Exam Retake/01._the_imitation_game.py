"""
During World War 2, you are a mathematician who has joined the cryptography team to decipher the
enemy's enigma code. Your job is to create a program to crack the codes.
On the first line of the input, you will receive the encrypted message. After that, until the "Decode"
 command is given, you will be receiving strings with instructions for different operations that need
  to be performed upon the concealed message to interpret it and reveal its true content. There are several
   types of instructions, split by '|'
•	"Move {number of letters}":
o	Moves the first n letters to the back of the string
•	"Insert {index} {value}":
o	Inserts the given value before the given index in the string
•	"ChangeAll {substring} {replacement}":
o	Changes all occurrences of the given substring with the replacement text
Input / Constraints
•	On the first line, you will receive a string with a message.
•	On the following lines, you will be receiving commands, split by '|' .
Output
•	After the "Decode" command is received, print this message:
"The decrypted message is: {message}"
"""




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