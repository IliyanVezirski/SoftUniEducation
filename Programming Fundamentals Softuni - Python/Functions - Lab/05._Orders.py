def total_cost(product, quantity):
    if product == "coffee":
        price = 1.5
    elif product == 'water':
        price = 1
    elif product == 'coke':
        price = 1.4
    elif product == 'snacks':
        price = 2
    return "{:.2f}".format(price * quantity)



product = input()
quantity = int(input())

print(total_cost(product, quantity))