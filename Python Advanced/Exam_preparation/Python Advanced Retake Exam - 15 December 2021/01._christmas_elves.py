"""
Everything in the Satna Claus' workshop was going well until, on one freezing Sunday, a dangerous storm destroyed almost
all toys. Now Santa's elves fear they won't be able to meet their December deadline. It could be a disaster, and some
children around the world may not get their Christmas toys. Luckily, you've come up with an idea, and you just need to
 write a program that manages your plan.
The Christmas elves have special toy-making skills - еach elf can make a toy from a given number of materials.
First, you will receive a sequence of integers representing each elf's energy. On the following line, you will be given
 another sequence of integers, each representing a number of materials in a box.
Your task is to calculate the total elves' energy used for making toys and the total number of successfully made toys.
You are very clever and have immediately recognized the pros and cons of the work process - the first elf takes the last
 box of materials and tries to create the toy:
•	Usually, the elf needs energy equal to the number of materials. If he has enough energy, he makes the toy. His energy
decreases by the used energy, and the toy goes straight to Santa's bag. Then, the elf eats a cookie reward which increases
 his energy by 1, and goes to the end of the line, preparing for the upcoming boxes.
•	Every third time one of the elves takes a box, he tries his best to be creative, and he will need twice as much energy
 as usual. If he has enough, he manages to create 2 toys. Then, his energy decreases; he eats a cookie reward and goes to
 the end of the line, similar to the first bullet.
•	Every fifth time one of the elves takes a box, he is a little clumsy and somehow manages to break the toy when he just
made it (if he made it). The toy is thrown away, and the elf doesn't get a cookie reward. However, his energy is already
 spent, and it needs to be added to the total elves' energy.
o	If an elf creates 2 toys, but he is clumsy, he breaks them.
•	If an elf does not have enough energy, he leaves the box of materials to the next elf. Instead of making the toy, the
elf drinks a hot chocolate which doubles his energy, and goes to the end of the line, preparing for the upcoming boxes.
Note: North Pole's social policy is very tolerant of the elves. If the current elf's energy is less than 5 units, he does
NOT TAKE a box, but he takes a day off. Remove the elf from the collection.
Stop crafting toys when you are out of materials or elves.
Input
•	The first line of input will represent each elf's energy - integers, separated by a single space
•	On the second line, you will be given the number of materials in each box - integers, separated by a single space
Output
•	On the first line, print the number of created toys: "Toys: {total_number_of_toys}"
•	On the second line, print the total used energy: "Energy: {total_used_energy}"
•	On the next two lines print the elves and boxes that are left, if there are any, otherwise skip the line:
o	"Elves left: {elf1}, {elf2}, … {elfN}"
o	"Boxes left: {box1}, {box2}, … {boxN}"
Constraints
•	All the elves' values will be integers in the range [1, 100]
•	All the boxes' values will be integers in the range [1, 100]

"""

from collections import deque

elfs_energy = deque(int(i) for i in input().split() if int(i) >= 5)
material_box = deque(int(i) for i in input().split())
total_energy_used = 0
total_toys = 0
counter = 0
while elfs_energy and material_box:
    to_break = False
    third_time = False
    counter += 1
    current_elf_energy = elfs_energy.popleft()
    while current_elf_energy < 5:
        if not elfs_energy:
            to_break = True
            break
        current_elf_energy = elfs_energy.popleft()
    if to_break:
        break
    current_material_box = material_box[-1]
    if counter % 3 == 0:
        third_time = True
        current_material_box *= 2
    if current_elf_energy >= current_material_box:
        current_elf_energy -= current_material_box
        if counter % 5 != 0:
            if third_time:
                total_toys += 2
            else:
                total_toys += 1
            current_elf_energy += 1
        total_energy_used += current_material_box
        elfs_energy.append(current_elf_energy)
        material_box.pop()
    else:
        current_elf_energy *= 2
        elfs_energy.append(current_elf_energy)
print(f"Toys: {total_toys}")
print(f"Energy: {total_energy_used}")
if elfs_energy:
    print(f"Elves left: {', '.join(list(map(str,elfs_energy)))}")
if material_box:
    print(f"Boxes left: {', '.join(list(map(str,material_box)))}")