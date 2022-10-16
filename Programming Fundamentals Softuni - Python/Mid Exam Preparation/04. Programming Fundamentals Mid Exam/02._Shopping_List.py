"""
It's the end of the week, and it is time for you to go shopping, so you need to create a shopping list first.
Input
You will receive an initial list with groceries separated by an exclamation mark "!".
After that, you will be receiving 4 types of commands until you receive "Go Shopping!".
•	"Urgent {item}" - add the item at the start of the list.  If the item already exists, skip this command.
•	"Unnecessary {item}" - remove the item with the given name, only if it exists in the list. Otherwise, skip this command.
•	"Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name with the new one.
Otherwise, skip this command.
•	"Rearrange {item}" - if the grocery exists in the list, remove it from its current position and add it at the
 end of the list. Otherwise, skip this command.
Constraints
•	There won't be any duplicate items in the initial list
Output
•	Print the list with all the groceries, joined by ", ":
"{firstGrocery}, {secondGrocery}, … {nthGrocery}"
"""
groceries = input().split("!")


def urgent(groceries: list, item: str):
    if item in groceries:
        return groceries
    else:
        groceries.insert(0, item)
        return groceries


def unnecessary(groceries: list, item: str):
    if item in groceries:
        groceries.remove(item)
        return groceries
    else:
        return groceries


def correct(groceries: list, old_item: str, new_item: str):
    if old_item in groceries:
        index_of_old_item = groceries.index(old_item)
        groceries[index_of_old_item] = new_item
    return groceries


def rearrange(groceries: list, item: str):
    if item in groceries:
        groceries.remove(item)
        groceries.append(item)
    return groceries


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
    if command == "Go Shopping!":
        break

print(*groceries, sep=', ')
