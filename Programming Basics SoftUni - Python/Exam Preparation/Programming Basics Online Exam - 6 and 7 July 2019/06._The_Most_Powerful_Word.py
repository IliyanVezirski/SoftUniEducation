import math
word = input()
winner_word = ''
winner_points = 0
while word != 'End of words':
    total_for_word = 0
    word_len = len(word)
    for i in word:
        letter = ord(i)
        total_for_word += letter
    first_letter = word[0]
    first_letter = first_letter.upper()
    first_letter = ord(first_letter)
    if first_letter == 65 or first_letter == 69 or first_letter == 73 or first_letter == 79 or first_letter == 85 or first_letter == 89:
        total_for_word *= word_len
    else:
        total_for_word = math.floor(total_for_word / word_len)
    if total_for_word > winner_points:
        winner_word = word
        winner_points = total_for_word
    word = input()
print(f'The most powerful word is {winner_word} - {winner_points}')