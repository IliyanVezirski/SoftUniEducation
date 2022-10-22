numbers = [int(i) for i in input().split()]
numbers = list(sorted(numbers))
result = []
average_number = sum(numbers) / len(numbers)

for i in range(len(numbers) - 1, 0, -1):
    if numbers[i] > average_number:
        result.append(numbers[i])
    if len(result) >= 5:
        break
if not result:
    print(f"No")
else:
    print(*result, sep=' ')
