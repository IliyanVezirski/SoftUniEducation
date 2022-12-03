def add(current_pieces: dict, current_piece: str, current_composer: str, current_key: str):
    if current_piece in current_pieces:
        print(f'{current_piece} is already in the collection!')
    else:
        current_pieces[current_piece] = {"composer": current_composer, "key": current_key}
        print(f"{current_piece} by {current_composer} in {current_key} added to the collection!")
    return current_pieces


def remove(current_pieces: dict, piece: str):
    if piece in current_pieces:
        print(f"Successfully removed {piece}!")
        del current_pieces[piece]
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")
    return current_pieces


def change_key(current_pieces: dict, current_piece: str, new_key: str):
    if current_piece in current_pieces:
        print(f"Changed the key of {current_piece} to {new_key}!")
        current_pieces[current_piece]['key'] = new_key
    else:
        print(f"Invalid operation! {current_piece} does not exist in the collection.")
    return current_pieces


pieces_info = {}
number_of_pieces = int(input())

for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    pieces_info[piece] = {"composer": composer, 'key': key}

command = input()
while command != "Stop":
    command = command.split("|")
    if command[0] == "Add":
        pieces_info = add(pieces_info, command[1], command[2], command[3])
    elif command[0] == "Remove":
        pieces_info = remove(pieces_info, command[1])
    elif command[0] == "ChangeKey":
        pieces_info = change_key(pieces_info, command[1], command[2])
    command = input()
[print(f"{piece} -> Composer: {stats['composer']}, Key: {stats['key']}") for piece, stats in pieces_info.items()]
