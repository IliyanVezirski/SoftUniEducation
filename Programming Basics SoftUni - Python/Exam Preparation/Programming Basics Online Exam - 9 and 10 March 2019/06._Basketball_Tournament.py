win_match = 0
lose_match = 0
all_match = 0
while True:
    tournament = input()
    if tournament == 'End of tournaments':
        print(f'{(win_match / all_match * 100):.2f}% matches win')
        print(f'{(lose_match / all_match * 100):.2f}% matches lost')
        break
    match_numbers = int(input())
    match_counter = 0
    for match in range(match_numbers):
        win_points = int(input())
        lose_points = int(input())
        match_counter += 1
        if win_points > lose_points:
            all_match += 1
            win_match += 1
            diff = win_points - lose_points
            print(f'Game {match_counter} of tournament {tournament}: win with {diff} points.')
        else:
            all_match += 1
            lose_match += 1
            diff = lose_points - win_points
            print(f'Game {match_counter} of tournament {tournament}: lost with {diff} points.')
