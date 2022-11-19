from collections import deque
quantity_of_food = int(input())
queue = deque([int(i) for i in input().split()])
biggest_costumer = max(queue)
while queue:
    if quantity_of_food - queue[0] < 0:
        break
    else:
        quantity_of_food -= queue.popleft()
print(biggest_costumer)
if queue:
    print(f"Orders left: {' '.join([str(i) for i in queue])}")
else:
    print(f"Orders complete")
