easter_bread = int(input())
name_baker = ''
winner = ''
winner_points = 0
points = 0
for bread in range(easter_bread):
    name_baker = input()
    points = 0
    while name_baker != 'Stop':
        evaluation = input()
        if evaluation == 'Stop':
            break
        evaluation = int(evaluation)
        points += evaluation
    print(f'{name_baker} has {points} points.')
    if points > winner_points:
        winner_points = points
        winner = name_baker
        print(f'{name_baker} is the new number 1!')
print(f'{winner} won competition with {winner_points} points!')
