statistics = input()
products = {}
while statistics != "statistics":
    statistics = statistics.split(":")
    product = statistics[0]
    quantity = int(statistics[1])
    if product not in products:
        products[product] = quantity
    else:
        products[product] += quantity
    statistics = input()
print(f"Products in stock:")
for product, quantity in products.items():
    print(f'- {product}: {quantity}')
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")