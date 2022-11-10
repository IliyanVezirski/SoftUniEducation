def add(current_pieces: dict, piece: str, composer: str, key: str):
    if piece in current_pieces:
        print(f"{piece} is already in the collection!")
    else:
        current_pieces[piece] = {composer: key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    return current_pieces


def remove(current_pieces: dict, piece: str):
    if piece in current_pieces:
        print(f"Successfully removed {piece}!")
        del current_pieces[piece]
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return current_pieces


def change(current_pieces: dict, piece: str, key: str):
    if piece in current_pieces:
        print(f"Changed the key of {piece} to {key}!")
        for song, composer in current_pieces.items():
            if song == piece:
                for comp in composer:
                    current_pieces[song][comp] = key
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return current_pieces


number_of_pieces = int(input())
pieces_dict = {}

for piece in range(number_of_pieces):
    data = input()
    data = data.split("|")
    pieces_dict[data[0]] = {data[1]: data[2]}

command = input()
while command != "Stop":
    command = command.split("|")
    if command[0] == "Add":
        pieces_dict = add(pieces_dict, command[1], command[2], command[3])
    elif command[0] == "Remove":
        pieces_dict = remove(pieces_dict, command[1])
    elif command[0] == "ChangeKey":
        pieces_dict = change(pieces_dict, command[1], command[2])
    command = input()
for piece, composer in pieces_dict.items():
    for comp, key in composer.items():
        print(f"{piece} -> Composer: {comp}, Key: {key}")

