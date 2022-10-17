gifts = input().split()


def outofstock(presents: list, item: str):
    if item in presents:
        for i in range(len(presents)):
            if presents[i] == item:
                presents[i] = None

    return presents


def required(presents: list, item: str, index: int):
    if index in range(len(presents)):
        presents[index] = item
    return presents


def justincase(presents: list, item: str):
    presents[-1] = item
    return presents


command = input()

while command != "No Money":
    command = command.split()
    gift = command[0]
    if gift == "OutOfStock":
        outofstock(gifts, command[1])
    elif gift == "Required":
        required(gifts, command[1], int(command[2]))
    elif gift == "JustInCase":
        justincase(gifts, command[1])
    command = input()

gifts = [i for i in gifts if i != None]
print(' '.join(gifts))
