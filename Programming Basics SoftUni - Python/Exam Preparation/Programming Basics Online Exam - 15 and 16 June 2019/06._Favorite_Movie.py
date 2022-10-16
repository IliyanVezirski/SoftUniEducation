favorite_movie = input()
movie_counter = 0
best_movie_points = 0
best_movie = ''
while favorite_movie != "STOP":
    movie_counter += 1
    if movie_counter >= 7:
        print(f'The limit is reached.')
        break
    point = 0
    points_sum = 0
    favorite_movie_len = len(favorite_movie)
    for letter in favorite_movie:
        points = ord(letter)
        if 65 <= points <= 90:
            points -= favorite_movie_len
        elif 97 <= points <= 122:
            points -= favorite_movie_len * 2
        points_sum += points
    if points_sum > best_movie_points:
        best_movie = favorite_movie
        best_movie_points = points_sum
    favorite_movie = input()
print(f'The best movie for you is {best_movie} with {best_movie_points} ASCII sum.')