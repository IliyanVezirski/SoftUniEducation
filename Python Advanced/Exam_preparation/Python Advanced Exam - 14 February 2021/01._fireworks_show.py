"""
First, you will be given a sequence of integers representing firework effects. Afterwards you will be given
 another sequence of integers representing explosive power.
You need to start from the first firework effect and try to mix it with the last explosive power.
 If the sum of their values is:
•	divisible by 3, but it is not divisible by 5 – create Palm firework and remove both materials
•	divisible by 5, but it is not divisible by 3 – create Willow firework and remove both materials
•	divisible by both 3 and 5 – create Crossette firework and remove both materials
Otherwise, decrease the value of the firework effect by 1 and move it at the end of the sequence. Then, try to mix
the same explosive power with the next firework effect.
If any value is equal to or below 0, you should remove it from the sequence before trying to mix it with the other.
When you have successfully prepared enough fireworks for the show or you have no more firework punches or explosive
power, you need to stop mixing.
To make the perfect firework show, Maria needs 3 of each of the firework types.
Input
•	On the first line, you will receive the integers representing the firework effects, separated by ", ".
•	On the second line, you will receive the integers representing the explosive power, separated by ", ".
Output
•	On the first line, print:
o	if Maria successfully prepared the firework show: "Congrats! You made the perfect firework show!"
o	if Maria failed to prepare it: "Sorry. You can't make the perfect firework show."
•	On the second line, print all firework effects left if there are any:
o	"Firework Effects left: {effect1}, {effect2}, (…)"
•	On the third line, print all explosive fillings left if there are any:
o	" Explosive Power left: {filling1}, {filling2}, (…)"
•	Then, you need to print all fireworks and the amount you have of them:
o	"Palm Fireworks: {count}"
o	"Willow Fireworks: {count}"
o	"Crossette Fireworks: {count}"
Constraints
•	All the given numbers will be integers in the range [-100, 100].
•	There will be no cases with empty sequences.

"""

from collections import deque


def check_if_successfully(fire_works: dict):
    for firework, count in fire_works.items():
        if count < 3:
            return False
    return True


fireworks_dict = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}

fireworks = deque([int(i) for i in input().split(", ") if int(i) > 0])
explosive = [int(i) for i in input().split(', ') if int(i) > 0]

while fireworks and explosive:
    if check_if_successfully(fireworks_dict):
        break
    current_firework = fireworks[0]
    current_explosive = explosive[-1]
    value_to_check = current_explosive + current_firework
    if value_to_check % 3 == 0 and value_to_check % 5 != 0:
        fireworks_dict['Palm Fireworks'] += 1
        fireworks.popleft()
        explosive.pop()
    elif value_to_check % 5 == 0 and value_to_check % 3 != 0:
        fireworks_dict['Willow Fireworks'] += 1
        fireworks.popleft()
        explosive.pop()
    elif value_to_check % 5 == 0 and value_to_check % 5 == 0:
        fireworks_dict['Crossette Fireworks'] += 1
        fireworks.popleft()
        explosive.pop()
    else:
        if current_firework - 1 > 0:
            fireworks.append(fireworks.popleft() - 1)
        else:
            fireworks.popleft()
if check_if_successfully(fireworks_dict):
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")
if fireworks:
    print(f"Firework effects left: {', '.join(list(map(str, fireworks)))}")
if explosive:
    print(f"Explosive Power left: {', '.join(list(map(str, explosive)))}")
[print(f"{firework}: {count}") for firework, count in fireworks_dict.items()]
