"""
Aladdin, rich and powerful with the help of the Genie, is now preparing to marry the princess Jasmine. He asks Genie for
help to prepare the wedding presents.
First, you will receive a sequence of integers representing the materials for every wedding present. After that, you
 will be given another sequence of integers – Genie magic level for every aim to make a gift.
Your task is to mix materials with magic levels so you can make presents, listed in the table below.
Gift	Magic needed
Gemstone	100 to 199
Porcelain Sculpture	200 to 299
Gold	300 to 399
Diamond Jewellery	400 to 499

To make a present, you should take the last integer of materials and sum it with the first magic level value.
If the result is between or equal to the numbers described in the table above, you make the corresponding gift and
remove both materials and magic value. Otherwise:
•	If the product of the operation is under 100:
o	And if it is an even number, double the materials, and triple the magic, then sum it again.
o	And if it is an odd number, double the sum of the materials and the magic level. Then, check again if it is between
 or equal to any of the numbers in the table above.
•	If the product of the operation is more than 499, divide the sum of the material and the magic level by 2.
Then, check again if it is between or equal to any of the numbers in the table above.
•	If, however, the result is not between or equal to any of the numbers in the table above after performing
the calculation, remove both the materials and the magic level.
Stop crafting gifts when you are out of materials or magic level.
You have succeeded in crafting the presents when you've crafted either one of the pairs - a gemstone and
a sculpture or gold and jewellery.
Input
•	The first line of input will represent the values of materials - integers, separated by a single space
•	On the second line, you will be given the magic levels - integers, separated by a single space
Output
•	On the first line - print whether you have succeeded in crafting the presents:
o	"The wedding presents are made!"
o	"Aladdin does not have enough wedding presents."
•	On the next two lines print the materials and magic that are left, if there are any, otherwise skip the line:
o	"Materials left: {material1}, {material2}, …"
o	"Magic left: {magicValue1}, {magicValue2}, …
•	On the next lines, print the gifts alphabetically that the Genie has crafted at least once:
"{present1}: {amount}
{present2}: {amount}
…
{presentN}: {amount}"
Constraints
•	All the materials values will be integers in the range [1, 1000]
•	Magic level values will be integers in the range [1, 1000]

"""

from collections import deque

materials = [int(i) for i in input().split()]
magic = deque(int(i) for i in input().split())
crafted_gifts = {}
pairs_to_check = {
    1: ['Gemstone', "Porcelain Sculpture"],
    2: ["Gold", 'Diamond Jewellery']
}
gifts = {
    "Gemstone": [100, 200],
    "Porcelain Sculpture": [200, 300],
    "Gold": [300, 400],
    "Diamond Jewellery": [400, 500]

}

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    sum_to_check = current_magic + current_material
    if sum_to_check > 499:
        sum_to_check /= 2
    elif sum_to_check < 100:
        if sum_to_check % 2 == 0:
            current_material = current_material * 2
            current_magic = 3 * current_magic
            sum_to_check = current_magic + current_material
        else:
            current_material *= 2
            current_magic *= 2
            sum_to_check = current_magic + current_material
    for gift, range_to_check in gifts.items():
        if range_to_check[0] <= sum_to_check < range_to_check[1] :
            if gift not in crafted_gifts:
                crafted_gifts[gift] = 0
            crafted_gifts[gift] += 1
            break
for item in crafted_gifts:
    for number, value in pairs_to_check.items():
        if item in value:
            pairs_to_check[number].remove(item)
if_collected_materials = False
for i,pairs in pairs_to_check.items():
    if not pairs:
        if_collected_materials = True

if if_collected_materials:
    print(f"The wedding presents are made!")
else:
    print(f'Aladdin does not have enough wedding presents.')
if materials:
    print(f"Materials left: {', '.join(list(map(str, materials)))}")
if magic:
    print(f"Magic left: {', '.join(list(map(str,magic)))}")
crafted_gifts = dict(sorted(crafted_gifts.items(), key=lambda x: x[0]))
[print(f"{item}: {count}") for item, count in crafted_gifts.items()]

