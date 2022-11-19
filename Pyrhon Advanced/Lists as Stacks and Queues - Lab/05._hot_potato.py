from collections import deque
children = deque(input().split())
potatoes_holder = int(input())
counter = 0
while len(children) != 1:
    counter += 1
    children.append(children.popleft())
    if counter == potatoes_holder:
        print(f"Removed {children.pop()}")
        counter = 0
print(f"Last is {''.join(children)}")