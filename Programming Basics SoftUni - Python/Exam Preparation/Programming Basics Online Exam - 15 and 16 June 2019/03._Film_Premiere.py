projection = input()
packet_for_movie = input()
tickets = int(input())
price = 0
if projection == 'John Wick':
    if packet_for_movie == 'Drink':
        price = 12
    elif packet_for_movie == 'Popcorn':
        price = 15
    elif packet_for_movie == 'Menu':
        price = 19
elif projection == 'Star Wars':
    if packet_for_movie == 'Drink':
        price = 18
    elif packet_for_movie == 'Popcorn':
        price = 25
    elif packet_for_movie == 'Menu':
        price = 30
elif projection == 'Jumanji':
    if packet_for_movie == 'Drink':
        price = 9
    elif packet_for_movie == 'Popcorn':
        price = 11
    elif packet_for_movie == 'Menu':
        price = 14
total_price = price * tickets
if projection == 'Star Wars' and tickets >= 4:
    total_price *= 0.70
elif projection == 'Jumanji' and tickets == 2:
    total_price *= 0.85
print(f'Your bill is {total_price:.2f} leva.')