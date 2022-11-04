"""
On the first line of the input, you will receive the concealed message. After that, until the "Reveal" command is given,
you will receive strings with instructions for different operations that need to be performed upon the concealed message
to interpret it and reveal its actual content. There are several types of instructions, split by ":|:"
•	"InsertSpace:|:{index}":
o	Inserts a single space at the given index. The given index will always be valid.
•	"Reverse:|:{substring}":
o	If the message contains the given substring, cut it out, reverse it and add it at the end of the message.
o	If not, print "error".
o	This operation should replace only the first occurrence of the given substring if there are two or more occurrences.
•	"ChangeAll:|:{substring}:|:{replacement}":
o	Changes all occurrences of the given substring with the replacement text.
Input / Constraints
•	On the first line, you will receive a string with a message.
•	On the following lines, you will be receiving commands, split by ":|:".
Output
•	After each set of instructions, print the resulting string.
•	After the "Reveal" command is received, print this message:
"You have a new text message: {message}"

"""


def insert_space(message: str, index: int):
    message_list = []
    for el in message:
        message_list.append(el)
    message_list.insert(index, " ")
    print(f"{''.join(message_list)}")
    return ''.join(message_list)


def reverse(message: str, substring: str):
    if substring in message:
        message = message.replace(substring, "", 1)
        substring = substring[::-1]
        message += substring
        print(message)
        return message
    else:
        print(f"error")
        return message


def change(message: str, substring: str, replacment: str):
    message = message.replace(substring, replacment)
    print(message)
    return message


concealed_message = input()

command = input()

while command != "Reveal":
    command = command.split(":|:")
    if command[0] == "InsertSpace":
        concealed_message = insert_space(concealed_message, int(command[1]))
    elif command[0] == "Reverse":
        concealed_message = reverse(concealed_message, command[1])
    elif command[0] == "ChangeAll":
        concealed_message = change(concealed_message, command[1], command[2])

    command = input()
print(f"You have a new text message: {concealed_message}")
