team_name = input()
played_games = int(input())
wins = 0
loses = 0
draws = 0
points = 0
if played_games == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    for games in range(played_games):
        result_from_game = input()
        if result_from_game == 'W':
            points += 3
            wins += 1
        elif result_from_game == 'D':
            points += 1
            draws += 1
        elif result_from_game == 'L':
            loses += 1
    wins_percentage = wins / played_games * 100
    print(f'{team_name} has won {points} points during this season.')
    print(f'Total stats:')
    print(f'## W: {wins}')
    print(f'## D: {draws}')
    print(f'## L: {loses}')
    print(f'Win rate: {wins_percentage:.2f}%')
