import re

string = input()
pattern = r'(?P<sep>[:]{2}|[*]{2})(?P<emoji>[A-Z][a-z]{2,})(?P=sep)'
pattern_for_threshold = r'\d'
cool_threshold = 1

threshold = re.findall(pattern_for_threshold, string)

for match in threshold:
    cool_threshold *= int(match)

coolness_of_emoji = re.findall(pattern, string)
cool_emoji = []
counter_of_emojies = 0
for match in coolness_of_emoji:
    current_cool = 0
    counter_of_emojies += 1
    for el in match[1]:
        current_cool += ord(el)
    if current_cool >= cool_threshold:
        cool_emoji.append(match)

print(f"Cool threshold: {cool_threshold}")
print(f"{counter_of_emojies} emojis found in the text. The cool ones are:")
[print(i[0]+i[1]+i[0]) for i in cool_emoji]