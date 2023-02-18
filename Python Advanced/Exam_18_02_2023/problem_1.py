from collections import deque

healing_items = {
    'Patch': 0,
    'Bandage': 0,
    'MedKit': 0,
}

textile = deque([int(i) for i in input().split()])
medicaments = deque([int(i) for i in input().split()])

while textile and medicaments:
    current_textile = textile[0]
    current_medicament = medicaments[-1]
    current_sum = current_medicament + current_textile
    if current_sum == 30:
        healing_items['Patch'] += 1
        textile.popleft()
        medicaments.pop()
        continue
    elif current_sum == 40:
        healing_items['Bandage'] += 1
        textile.popleft()
        medicaments.pop()
        continue
    elif current_sum == 100:
        healing_items['MedKit'] += 1
        textile.popleft()
        medicaments.pop()
        continue
    elif current_sum > 100:
        healing_items['MedKit'] += 1
        textile.popleft()
        medicaments.pop()
        medicaments[-1] += current_sum - 100
    else:
        textile.popleft()
        medicaments[-1] += 10
sorted_healing_items = dict(sorted(healing_items.items(), key=lambda x: (-x[1], x[0])))
if not medicaments and not textile:
    print(f'Textiles and medicaments are both empty.')
    [print(f'{name} - {count}') for name, count in sorted_healing_items.items() if count != 0]
elif not textile:
    print(f'Textiles are empty.')
    [print(f'{name} - {count}') for name, count in sorted_healing_items.items() if count != 0]
    print(f"Medicaments left: {', '.join(reversed([str(i) for i in medicaments]))}")
elif not medicaments:
    print(f'Medicaments are empty.')
    [print(f'{name} - {count}') for name, count in sorted_healing_items.items() if count != 0]
    print(f"Textiles left: {', '.join(list(map(str, textile  )))}")
