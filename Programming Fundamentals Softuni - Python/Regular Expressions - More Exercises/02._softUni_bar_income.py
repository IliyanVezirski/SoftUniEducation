import re

order = input()
costumers = {}
pattern_for_costumer = r'(?P<sep>%)(?P<costumer>[A-Z][a-z]+)(?P=sep)'
pattern_for_price = r'(?P<price>[0-9.]+)\$'
pattern_for_product = r'<(?P<product>[\w]+)>'
pattern_for_count = r'\|(?P<count>[0-9]+)\|'
verification = True
total = 0
while order != "end of shift":
    match_costumer = re.findall(pattern_for_costumer, order)
    match_price = re.findall(pattern_for_price, order)
    match_product = re.findall(pattern_for_product, order)
    match_count = re.findall(pattern_for_count, order)

    if match_costumer and match_price and match_count and match_product:
        current_total = int(match_count[0]) * float(match_price[0])
        total += current_total
        print(f"{match_costumer[0][1]}: {match_product[0]} - {current_total:.2f}")

    order = input()
print(f"Total income: {total:.2f}")