count_movies = int(input())
best_movie = ''
lowest_movie = ''
highest_rating = 0
lowest_rating = 10
total_rating = 0
for i in range(1, count_movies + 1 ):
    movie_name = input()
    movie_rating = float(input())
    total_rating += movie_rating
    if movie_rating > highest_rating:
        best_movie = movie_name
        highest_rating = movie_rating
    if movie_rating < lowest_rating:
        lowest_movie = movie_name
        lowest_rating = movie_rating

average_rating = total_rating / count_movies

print(f'{best_movie} is with highest rating: {highest_rating:.1f}')
print(f'{lowest_movie} is with lowest rating: {lowest_rating:.1f}')
print(f'Average rating: {average_rating:.1f}')