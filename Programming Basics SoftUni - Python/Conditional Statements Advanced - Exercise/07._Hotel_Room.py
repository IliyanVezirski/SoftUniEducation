month = input()
nights = int(input())
total_price_for_room = 0
total_price_for_studio = 0
if month == 'May' or month == 'October':
    total_price_for_room = 65 * nights
    total_price_for_studio = 50 * nights
elif month == 'June' or month == 'September':
    total_price_for_room = 68.70 * nights
    total_price_for_studio = 75.20 * nights
elif month == 'July' or month == 'August':
    total_price_for_room = 77 * nights
    total_price_for_studio = 76 * nights
if 7 < nights <= 14 and (month == 'May' or month == 'October'):
    total_price_for_studio *= 0.95
elif nights > 14 and (month == 'May' or month == 'October'):
    total_price_for_studio *= 0.70
if nights > 14 and (month == 'June' or month == 'September'):
    total_price_for_studio *= 0.80
if nights > 14:
    total_price_for_room *= 0.90
print(f'Apartment:{total_price_for_room: .2f} lv.')
print(f'Studio:{total_price_for_studio: .2f} lv.')