stage = input()
ticket_type = input()
ticket_number = int(input())
photo_with_trophy = input()
price = 0
if stage == 'Quarter final':
    if ticket_type == 'Standard':
        price = 55.50
    elif ticket_type == 'Premium':
        price = 105.20
    elif ticket_type == 'VIP':
        price = 118.90
elif stage == 'Semi final':
    if ticket_type == 'Standard':
        price = 75.88
    elif ticket_type == 'Premium':
        price = 125.22
    elif ticket_type == 'VIP':
        price = 300.40
elif stage == 'Final':
    if ticket_type == 'Standard':
        price = 110.10
    elif ticket_type == 'Premium':
        price = 160.66
    elif ticket_type == 'VIP':
        price = 400
total_price = price * ticket_number
if photo_with_trophy == 'Y':
    if total_price > 4000:
        total_price *= 0.75
    elif total_price > 2500:
        total_price = (total_price * 0.90) + (ticket_number * 40)
    else:
        total_price = total_price + ticket_number * 40
elif photo_with_trophy == 'N':
    if total_price > 4000:
        total_price *= 0.75
    elif total_price > 2500:
        total_price *= 0.90
print(f'{total_price:.2f}')