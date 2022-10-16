player_name = input()
points = 0
winner_points = 0
winner = ''

while player_name != 'Stop':
    points = 0
    for name in player_name:
        number = int(input())
        if ord(name) == number:
            points += 10
        else:
            points += 2
    if points >= winner_points:
        winner_points = points
        winner = player_name
    player_name = input()
print(f'The winner is {winner} with {winner_points} points!')