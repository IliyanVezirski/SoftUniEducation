materials_needed = {"shards": 0, "fragments": 0, "motes": 0}
junks = {}
item_obtained = False
crafted_item = ''
while not item_obtained:
    items = input().split()
    for index in range(0, len(items), 2):
        quantity = int(items[index])
        item_index = index + 1
        item = items[item_index].lower()
        if item == "shards" or item == "fragments" or item == "motes":
            materials_needed[item] += quantity
            if materials_needed[item] >= 250:
                materials_needed[item] -= 250
                item_obtained = True
                if item == "shards":
                    crafted_item = "Shadowmourne"
                    print(f"{crafted_item} obtained!")
                    break
                elif item == "fragments":
                    crafted_item = "Valanyr"
                    print(f"{crafted_item} obtained!")
                    break
                elif item == "motes":
                    crafted_item = "Dragonwrath"
                    print(f"{crafted_item} obtained!")
                    break
        else:
            if item not in junks:
                junks[item] = quantity
            else:
                junks[item] += quantity
for k, v in materials_needed.items():
    print(f"{k}: {v}")
for k, v in junks.items():
    print(f"{k}: {v}")
