hrizantemi = int(input())
roses = int(input())
lale = int(input())
season = input()
holiday = input()
hrizantemi_price = 0
roses_price = 0
lale_price = 0
total_price = 0
if season == 'Spring' or season == 'Summer':
    hrizantemi_price = 2
    roses_price = 4.10
    lale_price = 2.50
else:
    hrizantemi_price = 3.75
    roses_price = 4.50
    lale_price = 4.15
hrizantemi_total = hrizantemi * hrizantemi_price
roses_total = roses * roses_price
lale_total = lale * lale_price
total_price = hrizantemi_total + roses_total + lale_total
if holiday == 'Y':
    total_price *= 1.15
flowers = hrizantemi + roses + lale
if lale > 7 and season == 'Spring':
    total_price *= 0.95
if roses >= 10 and season =='Winter':
    total_price *= 0.90
if flowers > 20:
    total_price *= 0.80
print('% .2f' % (total_price + 2))