tournament_number = int(input())
start_points = int(input())
points = start_points
wins = 0
for tournaments in range(tournament_number):
    stage = input()
    if stage == 'W':
        wins += 1
        points += 2000
    elif stage == 'F':
        points += 1200
    elif stage == 'SF':
        points += 720
average_points = (points - start_points )/ tournament_number
percentage_wins = ('%.2f' % (wins / tournament_number * 100))
print(f'Final points: {points}')
print(f'Average points: {int(average_points)}')
print(f'{percentage_wins}%')