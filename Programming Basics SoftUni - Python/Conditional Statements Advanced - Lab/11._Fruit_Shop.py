fruit = input()
day = input()
quantity = float(input())
price = ''
if day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        price = str(('% .2f' % (2.70 * quantity)))
    elif fruit == 'apple':
        price = str(('% .2f' % (1.25 * quantity)))
    elif fruit == 'orange':
        price = str(('% .2f' % (0.90 * quantity)))
    elif fruit == 'grapefruit':
        price = str(('% .2f' % (1.60 * quantity)))
    elif fruit == 'kiwi':
        price = str(('% .2f' % (3.00 * quantity)))
    elif fruit == 'pineapple':
        price = str(('% .2f' % (5.60 * quantity)))
    elif fruit == 'grapes':
        price = str(('% .2f' % (4.20 * quantity)))
    else:
        price = 'error'
elif day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        price = str(('% .2f' % (2.50 * quantity)))
    elif fruit == 'apple':
        price = str(('% .2f' % (1.20 * quantity)))
    elif fruit == 'orange':
        price = str(('% .2f' % (0.85 * quantity)))
    elif fruit == 'grapefruit':
        price = str(('% .2f' % (1.45 * quantity)))
    elif fruit == 'kiwi':
        price = str(('% .2f' % (2.70 * quantity)))
    elif fruit == 'pineapple':
        price = str(('% .2f' % (5.50 * quantity)))
    elif fruit == 'grapes':
        price = str(('% .2f' % (3.85 * quantity)))
    else:
        price = 'error'
else:
    price = 'error'
print(price)
