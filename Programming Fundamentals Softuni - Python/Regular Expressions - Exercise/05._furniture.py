import re

items = []
command = input()
regex = r">>(?P<item>\w+)<<(?P<price>[0-9.]+)!(?P<quantity>[0-9.]+)"
total = 0
while command != "Purchase":
    if not re.findall(regex, command):
        command = input()
        continue

    item = re.findall(regex, command)
    item = item[0][0]
    items.append(item)
    price = re.findall(regex, command)
    price = float(price[0][1])
    quantity = re.findall(regex, command)
    quantity = int(quantity[0][2])
    total_price = quantity * price
    total += total_price
    command = input()
if items:
    print(f"Bought furniture:")
    print(*items, sep='\n')
    print(f'Total money spend: {total:.2f}')
