import re

text = input()
pattern = r'(?P<sep>[@#]{1})(?P<first_word>[A-za-z]{3,})(?P=sep)(?P=sep)(?P<second_word>[A-Za-z]{3,})'
matched_words = re.finditer(pattern, text)
matched = []
counter_of_match = 0
for match in matched_words:
    match = match.groupdict()
    counter_of_match += 1
    if match['first_word'][::-1] == match['second_word']:
        matched.append(f"{match['first_word']} <=> {match['second_word']}")
if counter_of_match > 0:
    print(f"{counter_of_match} word pairs found!")
else:
    print(f"No word pairs found!")
if matched:
    print("The mirror words are:")
    print(*matched, sep=', ')
else:
    print(f"No mirror words!")