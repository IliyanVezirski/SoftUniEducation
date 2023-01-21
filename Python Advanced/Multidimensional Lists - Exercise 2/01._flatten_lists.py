first_part = input().split('|')
result = []
for r in range(len(first_part) - 1, -1, -1):
    current = first_part[r].split()
    result += current
print(*result)