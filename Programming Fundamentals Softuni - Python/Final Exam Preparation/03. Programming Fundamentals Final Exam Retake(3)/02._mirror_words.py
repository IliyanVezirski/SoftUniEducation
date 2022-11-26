import re

text = input()
pattern = r'(?P<sep>[@]|[#])(?P<first_word>[A-Za-z]{3,})(?P=sep)(?P=sep)(?P<second_word>[A-Za-z]{3,})(?P=sep)'
counter_of_pairs = 0
matched_pairs = re.finditer(pattern, text)
mirror_words = []
for match in matched_pairs:
    match = match.groupdict()
    counter_of_pairs += 1
    if match['first_word'] == match['second_word'][::-1]:
        mirror_words.append(f"{match['first_word']} <=> {match['second_word']}")
if counter_of_pairs == 0:
    print(f'No word pairs found!')
else:
    print(f'{counter_of_pairs} word pairs found!')
if mirror_words:
    print("The mirror words are:")
    print(', '.join(mirror_words))
else:
    print(f'No mirror words!')
