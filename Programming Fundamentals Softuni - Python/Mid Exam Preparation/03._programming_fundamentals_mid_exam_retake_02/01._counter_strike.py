energy = int(input())
distance = input()
won_battles = 0
lose = False
while distance != "End of battle":
    distance = int(distance)
    if distance > energy:
        lose = True
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        break
    energy -= distance
    won_battles += 1
    if won_battles % 3 == 0:
        energy += won_battles
    distance = input()


if not lose:
    print(f"Won battles: {won_battles}. Energy left: {energy}")
