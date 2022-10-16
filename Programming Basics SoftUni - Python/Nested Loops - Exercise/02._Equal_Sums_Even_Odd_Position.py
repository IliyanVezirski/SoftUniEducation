first_number = int(input())
second_number = int(input())
for i in range(first_number, second_number + 1):
    i1 = i // 100000
    i2 = i % 100000 // 10000
    i3 = i % 10000 // 1000
    i4 = i % 1000 // 100
    i5 = i % 100 // 10
    i6 = i % 10
    if i1 + i3 + i5 == i2 + i4 +i6:
        print(i, end=' ')