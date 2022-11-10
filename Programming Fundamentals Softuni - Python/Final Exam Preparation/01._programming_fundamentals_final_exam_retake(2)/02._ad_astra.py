import re

pattern = r'(?P<sep>[\|]|[#])(?P<name>[A-Za-z\s]+)(?P=sep)(?P<date>[0-9]{2}/[0-9]{2}/[0-9]{2})(?P=sep)(?P<calories>[0-9]+)(?P=sep)'
string = input()
string = re.findall(pattern, string)
food = {
    'item': [],
    'date': [],
    'calories': []
}
for foods in string:
    food['item'].append(foods[1])
    food['date'].append(foods[2])
    food['calories'].append(int(foods[3]))
days = sum(food['calories']) // 2000
print(f"You have food to last you for: {days} days!")
for i in range(len(food['item'])):
    print(f"Item: {food['item'][i]}, Best before: {food['date'][i]}, Nutrition: {food['calories'][i]}")
