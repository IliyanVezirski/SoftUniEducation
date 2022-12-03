import re

pattern = r'(?P<sep>[@]|[#])(?P<first_word>[A-Za-z]+)(?P=sep)(?P=sep)(?P<second_word>[A-Za-z]+)(?P=sep)'

text = input()
matches = re.finditer(pattern, text)
counter_match = 0
mirror_words = []
for match in matches:
    match = match.groupdict()
    counter_match += 1
    if match['first_word'] == match['second_word'][::-1]:
        mirror_words.append(f"{match['first_word']} <=> {match['second_word']}")
if counter_match == 0:
    print(f"No word pairs found!")
    print(f"No mirror words!")
else:
    print(f"{counter_match} word pairs found!")
    if mirror_words:
        print(f"The mirror words are:")
        print(f"{', '.join(mirror_words)}")
    else:
        print(f"No mirror words!")
