def characters_between(character1,character2):
    character1 = ord(character1)
    character2 = ord(character2)
    final_letters = []
    for i in range(character1+1, character2):
        final_letters.append(chr(i))
    result = ' '.join(final_letters)
    return result



letter1 = input()
letter2 = input()
print(characters_between(letter1, letter2))