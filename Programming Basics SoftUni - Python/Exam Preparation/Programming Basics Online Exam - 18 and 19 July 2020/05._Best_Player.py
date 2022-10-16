player_name = input()
max_goals = 0
best_player = ''
total_goals = 0
while player_name != 'END':
    goals = int(input())
    if goals > max_goals:
        max_goals = goals
        best_player = player_name
    if goals >= 10:
        break
    player_name = input()
print(f'{best_player} is the best player!')
if max_goals >= 3:
    print(f'He has scored {max_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {max_goals} goals.')
