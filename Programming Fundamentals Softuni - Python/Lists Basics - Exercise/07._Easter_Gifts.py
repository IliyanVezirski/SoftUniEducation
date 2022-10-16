gifts = input().split()
command = input()
while command != "No Money":
    command = command.split()
    if command[0] == "OutOfStock":
        for i in gifts:
            if i == command[1]:
                i = gifts.index(i)
                gifts[i] = "None"
    if command[0] == "Required":
        index = int(command[2])
        index2 = len(gifts) - 1
        if index2 >= index:
            gifts[index] = command[1]
    if command[0] == "JustInCase":
        last_index = len(gifts) - 1
        gifts[last_index] = command[1]
    command = input()
while "None" in gifts:
    gifts.remove("None")
print(' '.join(gifts))