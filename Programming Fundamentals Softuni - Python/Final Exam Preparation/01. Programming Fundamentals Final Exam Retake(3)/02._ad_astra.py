import re

products = {
    "product": [],
    "date": [],
    "calories": []
}

string = input()
pattern = r'(?P<sep>[#]|[\|])(?P<product>[A-Za-z\s]+)(?P=sep)(?P<date>[0-9]{2}/[0-9]{2}/[0-9]{2})(?P=sep)(?P<calories>[0-9]+)(?P=sep)'

founded_products = re.finditer(pattern, string)
total_calories = 0
for match in founded_products:
    match = match.groupdict()

    products["product"].append(match['product'])
    products["date"].append(match['date'])
    products["calories"].append(match["calories"])
    total_calories += int(match['calories'])
print(f"You have food to last you for: {total_calories // 2000} days!")
[print(f"Item: {products['product'][i]}, Best before: {products['date'][i]}, Nutrition: {products['calories'][i]}") for
 i in range(len(products["product"]))]
