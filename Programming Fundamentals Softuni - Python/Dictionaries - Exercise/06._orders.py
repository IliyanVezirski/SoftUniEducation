products = {}

command = input()

while command != "buy":
    command = command.split()
    product = command[0]
    quantity = int(command[2])
    price = float(command[1])
    if product not in products:
        products[product] = [price, quantity]
    else:
        products[product][0] = price
        products[product][1] += quantity
    command = input()
for k, v in products.items():
    print(f"{k} -> {v[0] *v[1]:.2f}")