money = input()
increase = float(money)
if increase < 0:
    print(f'Invalid operation!')
total = 0
while money != 'NoMoreMoney' and increase > 0:
    increase = float(money)
    print(f'Increase: {increase:.2f}')
    total += increase
    money = input()
    if money == 'NoMoreMoney':
        break
    increase = float(money)
    if increase < 0:
        print(f'Invalid operation!')
        break
print(f'Total: {total:.2f}')