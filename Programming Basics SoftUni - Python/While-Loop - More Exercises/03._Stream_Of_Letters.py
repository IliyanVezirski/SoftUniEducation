letter = ''
letter_c_found = 0
letter_o_found = 0
letter_n_found = 0
key_letters = 0
word = ''
while letter != "End":
    letter = input()
    if key_letters % 3 == 0 and key_letters != 0:
        print(word, end=" ")
        key_letters = 0
        letter_n_found = 0
        letter_o_found = 0
        letter_c_found = 0
        word = ''
    if letter == 'End':
        break
    if letter == 'c' and letter_c_found < 1:
        letter_c_found += 1
        key_letters += 1
    elif letter == 'o' and letter_o_found < 1:
        letter_o_found += 1
        key_letters += 1
    elif letter == 'n' and letter_n_found < 1:
        letter_n_found += 1
        key_letters += 1
    else:
        if (65 <= ord(letter) <= 90) or (97 <= ord(letter) <= 122):
            word = word + letter