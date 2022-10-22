groceries = input().split("!")


def urgent(products: list, product: str):
    if product in products:
        return product
    else:
        products.insert(0, product)
    return product


def unnecessary(products: list, product: str):
    if product in products:
        products.remove(product)
        return products
    return products


def correct(products: list, old_item: str, new_item: str):
    if old_item in products:
        index_of_item = products.index(old_item)
        products[index_of_item] = new_item
        return products
    else:
        return products


def rearrange(products: list, product: str):
    if product in products:
        products.remove(product)
        products.append(product)
    return products


command = input()

while command != "Go Shopping!":
    command = command.split()
    if command[0] == "Urgent":
        urgent(groceries, command[1])
    elif command[0] == "Unnecessary":
        unnecessary(groceries, command[1])
    elif command[0] == "Correct":
        correct(groceries, command[1], command[2])
    elif command[0] == "Rearrange":
        rearrange(groceries, command[1])
    command = input()

print(*groceries, sep=', ')
