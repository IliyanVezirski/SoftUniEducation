budget = float(input())
season = input()
destination = ''
holiday = ''
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        budget *= 0.30
        holiday = 'Camp'
    elif season == 'winter':
        budget *= 0.70
        holiday = 'Hotel'
elif 100 < budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        budget *= 0.40
        holiday = 'Camp'
    elif season == 'winter':
        budget *= 0.80
        holiday = 'Hotel'
else:
    destination = 'Europe'
    budget *= 0.90
    holiday = 'Hotel'
print(f'Somewhere in {destination}')
print(holiday + ' -' + ('% .2f' % budget))
