"""Input / Constraints
You will receive a journal with some collecting items, separated with a comma and a space (", ").
After that, until receiving "Craft!" you will be receiving different commands split by " - ":
•	"Collect - {item}" - you should add the given item to your inventory. If the item already exists, you should skip this line.
•	"Drop - {item}" - you should remove the item from your inventory if it exists.
•	"Combine Items - {old_item}:{new_item}" - you should check if the old item exists.
If so, add the new item after the old one. Otherwise, ignore the command.
•	"Renew – {item}" – if the given item exists, you should change its position and put it last in your inventory.
Output
After receiving "Craft!" print the items in your inventory, separated by ", ".
"""

items = input().split(", ")


def collect(items: list, item: str):
    if item not in items:
        items.append(item)
    return items


def drop(items: list, item_to_drop: str):
    if item_to_drop in items:
        items.remove(item_to_drop)
    return items


def combine(items: list, old_item: str, new_item: str):
    if old_item in items:
        index_of_item = items.index(old_item)
        index_of_new_item = index_of_item + 1
        items.insert(index_of_new_item, new_item)
    return items

def renew(items: list, item: str):
    if item in items:
        items.remove(item)
        items.append(item)
    return items


craft = input()

while craft != "Craft!":
    craft = craft.split(' - ')
    command = craft[0]
    item = craft[1]
    if command == "Collect":
        collect(items, item)
    elif command == "Drop":
        drop(items, item)
    elif command == "Combine Items":
        item = item.split(':')
        old_item = item[0]
        new_item = item[1]
        combine(items, old_item, new_item)
    elif command == "Renew":
        renew(items, item)
    craft = input()

print(*items, sep=', ')
