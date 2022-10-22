houses = [int(i) for i in input().split('@')]

position = 0
jump = input()

while jump != "Love!":
    jump = jump.split()
    jump = int(jump[1])
    position += jump
    if position not in range(len(houses)):
        position = 0
    if houses[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        houses[position] -= 2
        if houses[position] == 0:
            print(f"Place {position} has Valentine's day.")
    jump = input()
mission_successful = [i for i in houses if i != 0]
print(f"Cupid's last position was {position}.")

if not mission_successful:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {len(mission_successful)} places.")
