def first_character_word(word: str):
    first_letter = ''
    new_word = []
    for n in word:
        if n.isnumeric():
            first_letter += n
        else:
            new_word.append(n)
    first_letter = chr(int(first_letter))
    new_word.insert(0,first_letter)
    return new_word


def character_changed_places(word: str):
    word = first_character_word(word)

    word[1], word[-1] = word[-1], word[1]

    return word

secret_message = input().split()
decipher_message = []
for i in secret_message:
    i = character_changed_places(i)

    decipher_message.append(''.join(i))
print(' '.join(decipher_message))

