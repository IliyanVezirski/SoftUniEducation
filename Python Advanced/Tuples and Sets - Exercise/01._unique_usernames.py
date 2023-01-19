names = int(input())
names_set = set()
for name in range(names):
    current_name = input()
    names_set.add(current_name)
print('\n'.join(names_set))
