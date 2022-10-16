def numbers():
    number = input().split()
    number_float = []
    for i in number:
        i = float(i)
        if i < 0:
            i = i * -1
        number_float.append(i)
    return number_float


print(numbers())