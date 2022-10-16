number_balls = int(input())
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
points = 0
other_colour = 0
for balls in range(number_balls):
    ball_colour = input()
    if ball_colour == 'red':
        red_balls += 1
        points += 5
    elif ball_colour == 'orange':
        orange_balls += 1
        points += 10
    elif ball_colour == 'yellow':
        yellow_balls += 1
        points += 15
    elif ball_colour == 'white':
        white_balls += 1
        points += 20
    elif ball_colour == 'black':
        black_balls += 1
        points /= 2
    else:
        other_colour += 1
print(f'Total points: {int(points)}')
print(f'Points from red balls: {red_balls}')
print(f'Points from orange balls: {orange_balls}')
print(f'Points from yellow balls: {yellow_balls}')
print(f'Points from white balls: {white_balls}')
print(f'Other colors picked: {other_colour}')
print(f'Divides from black balls: {black_balls}')