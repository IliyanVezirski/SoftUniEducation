list = input().split(', ')
list_without_zero = [int(n) for n in list]
counter = 0
for n in list:
    n = int(n)
    if n == 0:
        list_without_zero.remove(n)
        counter += 1
for j in range(counter):
    list_without_zero.append(0)


print(list_without_zero)
