"""The pirates need to carry a treasure chest safely back to the ship, looting along the way.
Create a program that manages the state of the treasure chest along the way. On the first line, you will receive the initial loot of
the treasure chest, which is a string of items separated by a "|".
"{loot1}|{loot2}|{loot3} … {lootn}"
The following lines represent commands until "Yohoho!" which ends the treasure hunt:
•	"Loot {item1} {item2}…{itemn}":
o	Pick up treasure loot along the way. Insert the items at the beginning of the chest.
o	If an item is already contained, don't insert it.
•	"Drop {index}":
o	Remove the loot at the given position and add it at the end of the treasure chest.
o	If the index is invalid, skip the command.
•	"Steal {count}":
o	Someone steals the last count loot items. If there are fewer items than the given count, remove as much as there are.
o	Print the stolen items separated by ", ":
"{item1}, {item2}, {item3} … {itemn}"
In the end, output the average treasure gain, which is the sum of all treasure items length divided by the count of all items inside the chest formatted to the second decimal point:
"Average treasure gain: {averageGain} pirate credits."
If the chest is empty, print the following message:
"Failed treasure hunt."
Input
•	On the 1st line, you are going to receive the initial treasure chest (loot separated by "|")
•	On the following lines, until "Yohoho!", you will be receiving commands.
Output
•	Print the output in the format described above.
Constraints
•	The loot items will be strings containing any ASCII code.
•	The indexes will be integers in the range [-200…200]
•	The count will be an integer in the range [1….100]
"""
treasure_chest = input().split("|")


def loot(chest: list, loot: list):
    for item in loot:
        if item not in chest:
            chest.insert(0, item)
    return chest


def drop(chest: list, index: int):
    if index in range(len(chest)):
        item = chest.pop(index)
        chest.append(item)
    return chest


def steal(chest: list, count: int):
    stealed_items = []
    if len(chest) - 1 <= count:
        print(*chest, sep=', ')
        print(f"Failed treasure hunt.")
        exit()
        return chest
    else:
        for item in range(count):
            steal = chest.pop(-1)
            stealed_items.append(steal)
        stealed_items = reversed(stealed_items)
    return stealed_items


command = input()

while command != "Yohoho!":
    command = command.split()
    case = command[0]
    if case == "Loot":
        loot(treasure_chest, command[1:])
    elif case == "Drop":
        drop(treasure_chest, int(command[1]))
    elif case == "Steal":
        stealed_items = steal(treasure_chest, int(command[1]))
    command = input()
averaga_treasure_gain = 0
for item in treasure_chest:
    averaga_treasure_gain += len(item)
averaga_treasure_gain = averaga_treasure_gain / len(treasure_chest)

print(*stealed_items, sep=', ')
print(f"Average treasure gain: {averaga_treasure_gain:.2f} pirate credits.")
