def move(current_text: str, number_of_letters: int):
    string_to_move = current_text[:number_of_letters]
    current_text = current_text[number_of_letters:]
    current_text = current_text + string_to_move
    return current_text


def insert(current_text: str, index: int, value: str):
    first_part = current_text[:index]
    second_part = current_text[index:]
    current_text = first_part + value + second_part
    return current_text


def change(current_text: str, substring: str, replacement: str):
    current_text = current_text.replace(substring,replacement)
    return current_text


text = input()

data = input()

while data != "Decode":
    data = data.split('|')
    if data[0] == "Move":
        text = move(text, int(data[1]))
    elif data[0] == "Insert":
        text = insert(text, int(data[1]), data[2])
    elif data[0] == "ChangeAll":
        text = change(text, data[1], data[2])
    data = input()

print(f"The decrypted message is: {text}")
