import re

pattern = r'(?P<sep>[=]|[/])(?P<destination>[A-Z][A-Za-z]{2,})(?P=sep)'

text = input()
total_points = 0
destinations = []

current_destinations = re.finditer(pattern, text)
for match in current_destinations:
    match = match.groupdict()
    destinations.append(match['destination'])
    total_points += len(match['destination'])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {total_points}")
