players = {}
data = input()

while data != "Season end":
    if "->" in data:
        data = data.split(' -> ')
        player = data[0]
        position = data[1]
        skill = int(data[2])
        if player not in players:
            players[player] = {position: skill}
        else:
            if position in players[player].keys():
                if players[player][position] < skill:
                    players[player][position] = skill
            else:
                players[player].update({position: skill})
    else:
        data = data.split(" vs ")
        player1 = data[0]
        player2 = data[1]
        if player1 in players.keys():
            if player2 in players.keys():
                player1_positions = []
                player2_positions = []
                for player1_position in players[player1].keys():
                    player1_positions.append(player1_position)
                for player2_position in players[player2].keys():
                    player2_positions.append(player2_position)
                for position_to_compare in player1_positions:
                    if position_to_compare in player2_positions:
                        if players[player1][position_to_compare] < players[player2][position_to_compare]:
                            del players[player1]
                            break
                        elif players[player2][position_to_compare] < players[player1][position_to_compare]:
                            del players[player2]
                            break
                        elif players[player2][position_to_compare] == players[player1][position_to_compare]:
                            continue
                        else:
                            continue

    data = input()
players_total_points = {}
for key, value in players.items():
    players_total_points[key] = 0
    for position, points in value.items():
        players_total_points[key] += points
players_total_points = dict(sorted(players_total_points.items(), key=lambda kvp: (-kvp[1], kvp[0])))

for player, position in players.items():
    players[player] = dict(sorted(position.items(), key=lambda kvp: (-kvp[1], kvp[0])))
sorted_players = {}
for sort in players_total_points:
    sorted_players[sort] = players[sort]
for player, position in sorted_players.items():
    print(f"{player}: {players_total_points[player]} skill")
    for pos, skill in position.items():
        print(f"- {pos} <::> {skill}")
