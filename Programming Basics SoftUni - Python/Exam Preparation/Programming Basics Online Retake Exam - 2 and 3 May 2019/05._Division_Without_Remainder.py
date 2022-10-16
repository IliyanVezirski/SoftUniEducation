number = int(input())
n2 = 0
n3 = 0
n4 = 0
for i in range(1, number+1):
    number1 = int(input())
    if number1 % 2 == 0:
        n2 += 1
    if number1 % 3 == 0:
        n3 += 1
    if number1 % 4 == 0:
        n4 +=1
percentage_n2 = n2 / number * 100
percentage_n3 = n3 / number * 100
percentage_n4 = n4 / number * 100
print(f'{percentage_n2:.2f}%')
print(f'{percentage_n3:.2f}%')
print(f'{percentage_n4:.2f}%')