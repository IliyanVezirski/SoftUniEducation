import re

pattern = r'(?P<sep>[#]|[|])(?P<item>[A-Za-z\s]+)(?P=sep)(?P<date>[0-9]{2}/[0-9]{2}/[0-9]{2})(?P=sep)(?P<calories>[0-9]+)(?P=sep)'
text = input()
matches = re.finditer(pattern, text)
total_calories = 0
items = {
    "products": [],
    "dates": [],
    "calories": []
}
for match in matches:
    match = match.groupdict()
    total_calories += int(match['calories'])
    items['products'].append(match['item'])
    items['dates'].append(match['date'])
    items['calories'].append(match['calories'])

print(f"You have food to last you for: {total_calories // 2000} days!")
for index in range(len(items['products'])):
    print(
        f"Item: {items['products'][index]}, Best before: {items['dates'][index]}, Nutrition: {items['calories'][index]}")
