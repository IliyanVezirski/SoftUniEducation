list1 = input().split()
dict = {}
for i in range(0 , len(list1) ,2):
    key = list1[i]
    value = list1[i +1]
    dict[key] = int(value)


print(f'{dict}')