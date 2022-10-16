number = int(input())
sum = 0
number_2 = 0
while number >= sum:
    sum += number_2
    if sum >= number:
        break
    number_2 = int(input())
print(sum)