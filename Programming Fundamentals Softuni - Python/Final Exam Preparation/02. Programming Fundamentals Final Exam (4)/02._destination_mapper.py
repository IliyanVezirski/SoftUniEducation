import re

text = input()
pattern = r'(?P<sep>[=]|[/])(?P<destination>[A-Z][A-z]{2,})(?P=sep)'
destinations = []
travel_points = 0

matches = re.finditer(pattern, text)

for match in matches:
    match = match.groupdict()
    destinations.append(match['destination'])
    travel_points += len(match['destination'])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")