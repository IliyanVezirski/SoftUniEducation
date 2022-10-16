name_movie = input()
hall_type = input()
count_tickets = int(input())

if hall_type == 'normal':
    if name_movie == 'A Star Is Born':
        price = 7.50
    elif name_movie == 'Bohemian Rhapsody':
        price = 7.35
    elif name_movie == 'Green Book':
        price = 8.15
    elif name_movie == 'The Favourite':
        price = 8.75
elif hall_type == 'luxury':
    if name_movie == 'A Star Is Born':
        price = 10.50
    elif name_movie == 'Bohemian Rhapsody':
        price = 9.45
    elif name_movie == 'Green Book':
        price = 10.25
    elif name_movie == 'The Favourite':
        price = 11.55
elif hall_type == 'ultra luxury':
    if name_movie == 'A Star Is Born':
        price = 13.50
    elif name_movie == 'Bohemian Rhapsody':
        price = 12.75
    elif name_movie == 'Green Book':
        price = 13.25
    elif name_movie == 'The Favourite':
        price = 13.95
total_price = price * count_tickets

print(f'{name_movie} -> {total_price:.2f} lv.')