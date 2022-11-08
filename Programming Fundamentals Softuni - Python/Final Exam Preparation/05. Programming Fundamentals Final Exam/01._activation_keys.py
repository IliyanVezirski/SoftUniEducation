"""
The first line of the input will be your raw activation key. It will consist of letters and numbers only.
After that, until the "Generate" command is given, you will be receiving strings with instructions for different operations that need
 to be performed upon the raw activation key.
There are several types of instructions, split by ">>>":
•	"Contains>>>{substring}":
o	If the raw activation key contains the given substring, prints: "{raw activation key} contains {substring}".
o	Otherwise, prints: "Substring not found!"
•	"Flip>>>Upper/Lower>>>{startIndex}>>>{endIndex}":
o	Changes the substring between the given indices (the end index is exclusive) to upper or lower case and then prints
the activation key.
o	All given indexes will be valid.
•	"Slice>>>{startIndex}>>>{endIndex}":
o	Deletes the characters between the start and end indices (the end index is exclusive) and prints the activation key.
o	Both indices will be valid.
Input
•	The first line of the input will be a string consisting of letters and numbers only.
•	After the first line, until the "Generate" command is given, you will be receiving strings.
Output
•	After the "Generate" command is received, print:
o	"Your activation key is: {activation key}"

"""


def contains(key: str, substring: str):
    if substring in key:
        print(f"{key} contains {substring}")
    else:
        print(f"Substring not found!")
    return key


def flip(key: str, command: str, start_point: int, end_point: int):
    if command == "Upper":
        string_for_change = key[start_point:end_point]
        string_for_change = string_for_change.upper()
    else:
        string_for_change = key[start_point:end_point]
        string_for_change = string_for_change.lower()
    first_part = key[:start_point]
    second_part = key[end_point:]
    key = first_part + string_for_change + second_part
    print(f"{key}")
    return key


def slice(key: str, start_point: int, end_point: int):
    new_first_part = key[:start_point]
    new_second_part = key[end_point:]
    key = new_first_part + new_second_part
    print(key)
    return key


activation_key = input()

data = input()
while data != "Generate":
    data = data.split('>>>')
    if data[0] == "Contains":
        activation_key = contains(activation_key, data[1])

    elif data[0] == "Flip":
        activation_key = flip(activation_key, data[1], int(data[2]), int(data[3]))
    elif data[0] == "Slice":
        activation_key = slice(activation_key, int(data[1]), int(data[2]))

    data = input()

print(f"Your activation key is: {activation_key}")
