first_player_name = input()
second_player_name = input()
points_first_player = 0
points_second_player = 0
is_true = True
while True:
    first_player_card = input()
    if first_player_card == 'End of game':
        break
    second_player_card = input()
    if second_player_card == 'End of game':
        break
    first_player_card = int(first_player_card)
    second_player_card = int(second_player_card)
    if first_player_card == second_player_card:
        print(f'Number wars!')
        is_true = False
        first_player_card = int(input())
        second_player_card = int(input())
        if first_player_card > second_player_card:
            print(f'{first_player_name} is winner with {points_first_player} points')
        else:
            print(f'{second_player_name} is winner with {points_second_player} points')
        break
    elif first_player_card > second_player_card:
        points_first_player += abs(first_player_card - second_player_card)
    elif second_player_card > first_player_card:
        points_second_player += abs(second_player_card - first_player_card)
if is_true:
    print(f'{first_player_name} has {points_first_player} points')
    print(f'{second_player_name} has {points_second_player} points')