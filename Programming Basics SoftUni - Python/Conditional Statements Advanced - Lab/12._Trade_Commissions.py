city = input()
value = float(input())
comission = ''
if city == 'Sofia':
    if 0 <= value <= 500:
        comission = str('% .2f' % (value * 0.05))
    elif 500 < value <= 1000:
        comission = str('% .2f' % (value * 0.07))
    elif 1000 < value <= 10000:
        comission = str('% .2f' % (value * 0.08))
    elif value > 10000:
        comission = str('% .2f' % (value * 0.12))
    else:
        comission = 'error'
elif city == 'Varna':
    if 0 <= value <= 500:
        comission = str('% .2f' % (value * 0.045))
    elif 500 < value <= 1000:
        comission = str('% .2f' % (value * 0.075))
    elif 1000 < value <= 10000:
        comission = str('% .2f' % (value * 0.10))
    elif value > 10000:
        comission = str('% .2f' % (value * 0.13))
    else:
        comission = 'error'
elif city == 'Plovdiv':
    if 0 <= value <= 500:
        comission = str('% .2f' % (value * 0.055))
    elif 500 < value <= 1000:
        comission = str('% .2f' % (value * 0.08))
    elif 1000 < value <= 10000:
        comission = str('% .2f' % (value * 0.12))
    elif value > 10000:
        comission = str('% .2f' % (value * 0.145))
    else:
        comission = 'error'
else:
    comission = 'error'
print(comission)