age = float(input())
gender = input()
n = ''
if gender == 'm':
    if age >= 16:
        n = 'Mr.'
    else:
        n = 'Master'
if gender == 'f':
    if age >= 16:
        n = 'Ms.'
    else:
        n = 'Miss'

print(n)