teamA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
teamB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

cards = input().split()

is_stopped = False
for i in cards:
    i = i.split('-')
    team_player = int(i[1])
    if i[0] == "A" and team_player in teamA:
        teamA.remove(team_player)
    elif i[0] == "B" and team_player in teamB:
        teamB.remove(team_player)
    if len(teamA) < 7 or len(teamB) < 7:
        is_stopped = True
        break
print(f'Team A - {len(teamA)}; Team B - {len(teamB)}')
if is_stopped:
    print("Game was terminated")