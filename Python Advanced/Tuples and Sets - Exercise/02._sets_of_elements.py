number_of_elements = list(map(int, input().split()))
first_set = set()
second_set = set()
for i in range(1, sum(number_of_elements) + 1):
    element = input()
    if i <= number_of_elements[0]:
        first_set.add(element)
    else:
        second_set.add(element)
if len(first_set) >= len(second_set):
    print(*[str(i) for i in first_set if i in second_set], sep='\n')
else:
    print(*[str(i) for i in second_set if i in first_set], sep='\n')
