
items = {}
while True:
    resources = input()
    if resources == "stop":
        break
    quantity = int(input())
    if resources not in items:
        items[resources] = quantity
    else:
        items[resources] += quantity


for k, v in items.items():
    print(f"{k} -> {v}")
