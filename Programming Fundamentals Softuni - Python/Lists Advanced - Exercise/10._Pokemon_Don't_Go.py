numbers = [int(i) for i in input().split()]

result = []
def index_less_0(list: list):
    element_value = list[-1]
    list[0] = list[-1]
    result.append(element_value)
    for i, n in enumerate(list):
        if n <= element_value:
            list[i] += element_value
        else:
            list[i] -= element_value
    return list


def index_greater_last(list: list):
    element_value = list[0]
    list[-1] = list[0]
    result.append(element_value)
    for i, n in enumerate(list):
        if n <= element_value:
            list[i] += element_value
        else:
            list[i] -= element_value
    return list

def index_in_range(list: list,index: int):
    element_value = list[index]
    result.append(element_value)
    for i, n in enumerate(list):
        if n <= element_value:
            list[i] += element_value
        else:
            list[i] -= element_value
    list.pop(index)
    return list


command = int(input())
while numbers != []:
    if command >= len(numbers):
        index_greater_last(numbers)
    elif command < 0:
        index_less_0(numbers)
    else:
        index_in_range(numbers,command)
    if numbers == []:
        break
    command = int(input())


print(sum(result))