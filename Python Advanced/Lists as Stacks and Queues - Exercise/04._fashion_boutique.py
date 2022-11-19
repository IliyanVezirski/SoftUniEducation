from collections import deque

box_of_clothes = [int(i) for i in input().split()]
box_capacity = int(input())
capacity = 0
current_capacity = []
while box_of_clothes:
    current_clothe = box_of_clothes.pop()
    if sum(current_capacity) + current_clothe > box_capacity:
        capacity += 1
        current_capacity = []
        current_capacity.append(current_clothe)
    else:
        current_capacity.append(current_clothe)
print(capacity + 1)
