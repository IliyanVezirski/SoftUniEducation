from collections import deque

working_bees = deque(int(i) for i in input().split())
nectar = [int(i) for i in input().split()]
honey_making_process = deque(input().split())
result = 0
while working_bees and nectar:
    current_bee = working_bees[0]
    current_nectar = nectar[-1]
    if current_nectar >= current_bee:
        if working_bees:
            working_bees.popleft()
        if nectar:
            nectar.pop()
        to_do = honey_making_process.popleft()
        if to_do == "+":
            result += abs(current_bee + current_nectar)
        elif to_do == "-":
            result += abs(current_bee - current_nectar)
        elif to_do == '/':
            if current_bee != 0 and current_nectar != 0:
                result += abs(current_bee / current_nectar)
        elif to_do == '*':
            result += abs(current_bee * current_nectar)

    else:
        if nectar:
            nectar.pop()

print(f'Total honey made: {result}')
if nectar:
    print(f"Nectar left: {', '.join(list(map(str, nectar)))}")
if working_bees:
    print(f"Bees left: {', '.join(list(map(str, working_bees)))}")
