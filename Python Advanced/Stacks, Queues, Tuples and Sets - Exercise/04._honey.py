from collections import deque

working_bees = deque(int(i) for i in input().split())
nectar = [int(i) for i in input().split()]
honey_making_process = deque(input().split())
result = 0
while True:
    if not nectar or not working_bees:
        break
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()
    while current_nectar < current_bee:
        current_nectar = nectar.pop()
        if not nectar:
            break
    to_do = honey_making_process.popleft()
    if to_do == "-":
        result += abs(current_bee - current_nectar)
    elif to_do == '+':
        result += abs(current_bee + current_nectar)
    elif to_do == "/":
        result += abs(current_bee / current_nectar)
    elif to_do == "*":
        result += abs(current_bee * current_nectar)
print(f'Total honey made: {result}')
if nectar:
    print(f"Nectar left: {', '.join(list(map(str, nectar)))}")
if working_bees:
    print(f"Bees left: {', '.join(list(map(str, working_bees)))}")
