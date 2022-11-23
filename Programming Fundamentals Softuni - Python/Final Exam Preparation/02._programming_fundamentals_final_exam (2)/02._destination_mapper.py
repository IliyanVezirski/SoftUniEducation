import re

string = input()

pattern = r'(?P<sep>[=|/])(?P<word>[A-Z][A-za-z]{2,})(?P=sep)'

matches = re.finditer(pattern, string)
destinations = []
points = 0
for match in matches:
    match.groupdict()
    destinations.append(match['word'])
    points += len(match['word'])
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")