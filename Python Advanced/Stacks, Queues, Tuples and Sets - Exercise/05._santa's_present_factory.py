from collections import deque

boxes_with_materials = [int(i) for i in input().split()]
magic_values = deque(int(i) for i in input().split())
presents = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0
}
current_box = 0
current_magic = 0
while boxes_with_materials and magic_values:
    flag = False
    if boxes_with_materials[-1] == 0:
        flag = True
        boxes_with_materials.pop()
    if magic_values[0] == 0:
        magic_values.popleft()
        flag = True
    if flag:
        continue
    magic_level = boxes_with_materials[-1] * magic_values[0]
    if magic_level == 150:
        presents['Doll'] += 1
        boxes_with_materials.pop()
        magic_values.popleft()
        continue
    elif magic_level == 250:
        presents['Wooden train'] += 1
        boxes_with_materials.pop()
        magic_values.popleft()
        continue
    elif magic_level == 300:
        presents['Teddy bear'] += 1
        boxes_with_materials.pop()
        magic_values.popleft()
        continue
    elif magic_level == 400:
        presents['Bicycle'] += 1
        boxes_with_materials.pop()
        magic_values.popleft()
        continue
    if magic_level < 0:
        boxes_with_materials.append(boxes_with_materials.pop() + magic_values.popleft())
    elif magic_level > 0:
        boxes_with_materials[-1] += 15
        magic_values.popleft()
crafted_presents = {}
for present, crafted in presents.items():
    if crafted > 0:
        crafted_presents[present] = crafted

if (
        'Doll' in crafted_presents.keys() and "Wooden train" in crafted_presents.keys()) or "Teddy bear" in crafted_presents.keys() \
        and "Bicycle" in crafted_presents.keys():
    print(f"The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if boxes_with_materials:
    print(f"Materials left: {', '.join([str(boxes_with_materials[i]) for i in range(len(boxes_with_materials) - 1, -1, -1)])}")
if magic_values:
    print(f"Magic left: {', '.join(list(map(str, magic_values)))}")
crafted_presents = list(sorted(crafted_presents.keys()))
for present in crafted_presents:
    print(f"{present}: {presents[present]}")