def add_piece(current_pieces: dict, piece_to_add: str, composer_to_add: str, key_to_add: str):
    if piece_to_add not in current_pieces:
        current_pieces[piece_to_add] = {"composer": composer_to_add, "key": key_to_add}
        print(f"{piece_to_add} by {composer_to_add} in {key_to_add} added to the collection!")
    else:
        print(f"{piece_to_add} is already in the collection!")
    return current_pieces


def remove_piece(current_pieces: dict, pieces_to_remove: str):
    if pieces_to_remove not in current_pieces:
        print(f"Invalid operation! {pieces_to_remove} does not exist in the collection.")
    else:
        del current_pieces[pieces_to_remove]
        print(f"Successfully removed {pieces_to_remove}!")
    return current_pieces


def change_key_piece(current_pieces: dict, piece_to_change: str, key_to_change: str):
    if piece_to_change not in current_pieces:
        print(f"Invalid operation! {piece_to_change} does not exist in the collection.")
    else:
        current_pieces[piece_to_change]["key"] = key_to_change
        print(f"Changed the key of {piece_to_change} to {key_to_change}!")
    return current_pieces


pieces_dict = {}

number_of_pieces = int(input())

for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    pieces_dict[piece] = {"composer": composer, "key": key}

command = input()

while command != "Stop":
    command = command.split("|")
    if command[0] == "Add":
        pieces_dict = add_piece(pieces_dict, command[1], command[2], command[3])
    elif command[0] == "Remove":
        pieces_dict = remove_piece(pieces_dict, command[1])
    elif command[0] == "ChangeKey":
        pieces_dict = change_key_piece(pieces_dict, command[1], command[2])
    command = input()

[print(f"{piece} -> Composer: {stats['composer']}, Key: {stats['key']}") for piece, stats in pieces_dict.items()]
