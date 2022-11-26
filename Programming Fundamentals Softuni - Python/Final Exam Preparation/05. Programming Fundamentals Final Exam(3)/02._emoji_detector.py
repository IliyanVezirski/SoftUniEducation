import re

text = input()
pattern = r'(?P<sep>[:]{2}|[\*]{2})(?P<emoji>[A-Z][a-z]{2,})(?P=sep)'
threshold_pattern = r'\d'
threshold_matches = re.findall(threshold_pattern, text)
points_threshold = 1
founded_emoji = 0
cool_emojies = []
for match in threshold_matches:
    points_threshold *= int(match)

emoji_match = re.finditer(pattern, text)
for match in emoji_match:
    founded_emoji += 1
    match = match.groupdict()
    current_coolness = 0
    for letter in match['emoji']:
        current_coolness += ord(letter)
    if current_coolness >= points_threshold:
        cool_emojies.append(f"{match['sep']}{match['emoji']}{match['sep']}")
print(f"Cool threshold: {points_threshold}")

print(f"{founded_emoji} emojis found in the text. The cool ones are:")
print('\n'.join(cool_emojies))
