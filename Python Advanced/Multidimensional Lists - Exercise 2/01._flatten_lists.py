first_part = input().split('|')
second_part = [[i for i in first_part[r].split()] for r in range(len(first_part) - 1, -1, -1)]
for r in second_part:
    print(*r,end=' ')
