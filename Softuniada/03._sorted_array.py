elements_of_data = int(input())
elements = list(map(int, input().split()))
sorted_list = []
if elements_of_data % 2 == 0:
    for index in range(0, len(elements), 2):
        sorted_list.append(max(elements[index], elements[index + 1]))
        sorted_list.append(min(elements[index], elements[index + 1]))
else:
    for index in range(0, len(elements)-1, 2):
        sorted_list.append(max(elements[index], elements[index + 1]))
        sorted_list.append(min(elements[index], elements[index + 1]))
    sorted_list.append(elements[-1])

print(' '.join([str(el) for el in sorted_list]))
