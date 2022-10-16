project = input()
row = int(input())
colums = int(input())
income = 0
cinema_capacity = row * colums
if project == 'Premiere':
    income = cinema_capacity * 12
elif project == 'Normal':
    income = cinema_capacity * 7.50
elif project == 'Discount':
    income = cinema_capacity * 5
print('% .2f' % income + ' leva')