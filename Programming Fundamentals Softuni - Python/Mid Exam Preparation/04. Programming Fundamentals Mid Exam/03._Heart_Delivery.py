"""Valentine's day is coming, and Cupid has minimal time to spread some love across the neighborhood. Help him with his mission!
You will receive a string with even integers, separated by a "@" - this is our neighborhood. After that, a series of Jump
commands will follow until you receive "Love!". Every house in the neighborhood needs a certain number of hearts delivered by
Cupid so it can celebrate Valentine's day. The integers in the neighborhood indicate those needed hearts.
Cupid starts at the position of the first house (index 0) and must jump by a given length. The jump commands
will be in this format: "Jump {length}".
Every time he jumps from one house to another, the needed hearts for the visited house are decreased by 2:
•	If the needed hearts for a certain house become equal to 0, print on the console "Place {house_index} has Valentine's day."
•	If Cupid jumps to a house where the needed hearts are already 0, print on the console "Place {house_index} already had Valentine's day."
•	Keep in mind that Cupid can have a larger jump length than the size of the neighborhood, and if he does jump outside of it,
 he should start from the first house again (index 0)
For example, we are given this neighborhood: 6@6@6. Cupid is at the start and jumps with a length of 2. He will end up at index 2
 and decrease the needed hearts by 2: [6, 6, 4]. Next, he jumps again with a length of 2 and goes outside the neighborhood,
 so he goes back to the first house (index 0) and again decreases the needed hearts there: [4, 6, 4].
"""

neighborhood = [int(i) for i in input().split('@')]

position = 0

command = input()

while command != "Love!":
    command = command.split()
    jump = int(command[1])
    if jump + position > len(neighborhood) - 1:
        position = 0
    else:
        position += jump
    if neighborhood[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        neighborhood[position] -= 2
        if neighborhood[position] == 0:
            print(f"Place {position} has Valentine's day.")
    command = input()

valentines_houses = [i for i in neighborhood if i == 0]
print(f"Cupid's last position was {position}.")
if len(valentines_houses) == len(neighborhood):
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {len(neighborhood) - len(valentines_houses)} places.")
