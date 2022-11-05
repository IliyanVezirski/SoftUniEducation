import re

pattern = r'(?P<Day>\d{2})(?P<Sep>[/\.-])(?P<Month>[A-Z][a-z]{2})(?P=Sep)(?P<Year>\d{4})'

dates = input()

date = re.finditer(pattern, dates)
date_to_print = {"day": [], "month": [], "year": []}

for i in date:
    date_to_print["day"].append(i["Day"])
    date_to_print["month"].append(i["Month"])
    date_to_print["year"].append(i["Year"])
for i in range(len(date_to_print["day"])):
    print(f"Day: {date_to_print['day'][i]}, Month: {date_to_print['month'][i]}, Year: {date_to_print['year'][i]}")

