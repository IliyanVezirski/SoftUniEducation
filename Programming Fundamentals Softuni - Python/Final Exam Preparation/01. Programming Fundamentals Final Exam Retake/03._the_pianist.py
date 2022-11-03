"""
You are a pianist, and you like to keep a list of your favorite piano pieces. Create a program to help you organize it
and add, change, remove pieces from it!
On the first line of the standard input, you will receive an integer n – the number of pieces you will initially have.
On the next n lines, the pieces themselves will follow with their composer and key, separated by "|" in the following format:
"{piece}|{composer}|{key}".
Then, you will be receiving different commands, each on a new line, separated by "|", until the "Stop" command is given:
•	"Add|{piece}|{composer}|{key}":
o	You need to add the given piece with the information about it to the other pieces and print:
"{piece} by {composer} in {key} added to the collection!"
o	If the piece is already in the collection, print:
"{piece} is already in the collection!"
•	"Remove|{piece}":
o	If the piece is in the collection, remove it and print:
"Successfully removed {piece}!"
o	Otherwise, print:
"Invalid operation! {piece} does not exist in the collection."
•	"ChangeKey|{piece}|{new key}":
o	If the piece is in the collection, change its key with the given one and print:
"Changed the key of {piece} to {new key}!"
o	Otherwise, print:
"Invalid operation! {piece} does not exist in the collection."
Upon receiving the "Stop" command, you need to print all pieces in your collection in the following format:
"{Piece} -> Composer: {composer}, Key: {key}"
Input/Constraints
•	You will receive a single integer at first – the initial number of pieces in the collection
•	For each piece, you will receive a single line of text with information about it.
•	Then you will receive multiple commands in the way described above until the command "Stop".
Output
•	All the output messages with the appropriate formats are described in the problem description.
"""


def add(information: dict, piece: str, composer: str, key: str):
    if piece not in information.keys():
        information[piece] = [composer, key]
        print(f"{piece} by {composer} in {key} added to the collection!")
    else:
        print(f"{piece} is already in the collection!")
    return information


def remove(information: dict, piece: str):
    if piece in information.keys():
        information.pop(piece)
        print(f"Successfully removed {piece}!")
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return information


def change(information: dict, piece: str, new_key):
    if piece in information:
        old_value = information[piece][0]
        information[piece] = [old_value, new_key]
        print(f"Changed the key of {piece} to {new_key}!")
    else:

        print(f"Invalid operation! {piece} does not exist in the collection.")
    return information


collection = {}

pieces = int(input())

for i in range(pieces):
    compositor = input().split("|")
    collection[compositor[0]] = [compositor[1], compositor[2]]

command = input()

while command != "Stop":
    command = command.split("|")
    if command[0] == "Add":
        collection = add(collection, command[1], command[2], command[3])
    elif command[0] == "Remove":
        collection = remove(collection, command[1])
    elif command[0] == "ChangeKey":
        collection = change(collection, command[1], command[2])
    command = input()
for key, value in collection.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
