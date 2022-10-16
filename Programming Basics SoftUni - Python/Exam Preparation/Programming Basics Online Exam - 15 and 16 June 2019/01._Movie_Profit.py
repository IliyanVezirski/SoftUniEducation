movie = input()
days = int(input())
tickets = int(input())
price_tickets = float(input())
for_cinema = int(input())
percentage_for_cinema = for_cinema / 100
tickets_price_for_day = tickets * price_tickets
total_from_tickets = tickets_price_for_day * days
total = total_from_tickets - (total_from_tickets * percentage_for_cinema)
print(f'The profit from the movie {movie} is {total:.2f} lv.')