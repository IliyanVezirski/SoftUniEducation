sold_games = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
other = 0
for games in range(sold_games):
    game = input()
    if game == 'Hearthstone':
        hearthstone += 1
    elif game == 'Fornite':
        fornite += 1
    elif game == 'Overwatch':
        overwatch += 1
    else:
        other += 1
percentage_hearthstone = hearthstone / sold_games * 100
percentage_fornite = fornite / sold_games * 100
percentage_overwatch = overwatch / sold_games * 100
percentage_other = other / sold_games * 100
print(f'Hearthstone - {percentage_hearthstone:.2f}%')
print(f'Fornite - {percentage_fornite:.2f}%')
print(f'Overwatch - {percentage_overwatch:.2f}%')
print(f'Others - {percentage_other:.2f}%')
