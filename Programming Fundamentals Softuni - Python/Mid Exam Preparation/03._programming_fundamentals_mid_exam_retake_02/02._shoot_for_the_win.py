sequence = [int(i) for i in input().split()]

shoot = input()

while shoot != "End":
    shoot = int(shoot)
    if shoot in range(len(sequence)):
        item_to_calculate = sequence[shoot]
        sequence[shoot] = -1
        if item_to_calculate == -1:
            continue

        else:

            for number in range(len(sequence)):
                if sequence[number] == -1:
                    continue
                elif sequence[number] > item_to_calculate:
                    sequence[number] -= item_to_calculate
                elif sequence[number] <= item_to_calculate:
                    sequence[number] += item_to_calculate
    shoot = input()
shot_targets = len([i for i in sequence if i == -1])
print(f"Shot targets: {shot_targets} -> {' '.join(str(i) for i in sequence)}")
