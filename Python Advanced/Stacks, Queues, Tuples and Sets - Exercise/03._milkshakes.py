from collections import deque

chocolate = [int(i) for i in input().split(', ')]
cups_of_milk = deque(int(i) for i in input().split(', '))
milkshakes = 0
while chocolate and cups_of_milk:
    while chocolate[-1] <= 0:
        chocolate.pop()
        if not chocolate:
            break
    while cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        if not cups_of_milk:
            break
    if not chocolate or not cups_of_milk:
        break
    current_chocolate = chocolate[-1]
    current_cup_of_milk = cups_of_milk.popleft()
    if current_chocolate == current_cup_of_milk:
        milkshakes +=1
        chocolate.pop()
    else:
        cups_of_milk.append(current_cup_of_milk)
        chocolate[-1] -= 5
    if milkshakes == 5:
        break

if milkshakes == 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print(f'Not enough milkshakes.')
if chocolate:
    print(f"Chocolate: {', '.join(list(map(str, chocolate)))}")
else:
    print(f'Chocolate: empty')
if cups_of_milk:
    print(f"Milk: {', '.join(list(map(str,cups_of_milk)))}")
else:
    print(f'Milk: empty')