number_of_names = int(input())
odd_set = set()
even_set = set()

for i in range(1, number_of_names + 1):
    current_name = input()
    current_sum = int(sum([ord(i) for i in current_name]) / i)
    if current_sum % 2 == 0:
        even_set.add(current_sum)
    else:
        odd_set.add(current_sum)
if sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')
elif sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=', ')
else:
    print(*even_set.symmetric_difference(odd_set), sep=', ')
