tabs = int(input())
salary = int(input())
fine = 0
for i in range(1, tabs+1):
    tab_name = input()
    if tab_name == 'Facebook':
        fine += 150
    if tab_name == 'Instagram':
        fine += 100
    if tab_name == 'Reddit':
        fine += 50
    if fine >= salary:
        print(f'You have lost your salary.')
        break
if fine < salary:
    diff = abs(salary - fine)
    print(f'{diff}')