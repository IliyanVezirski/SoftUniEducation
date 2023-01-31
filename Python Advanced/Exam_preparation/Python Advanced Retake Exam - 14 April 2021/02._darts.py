"""
You will be given a matrix with 7 rows and 7 columns representing the dartboard. For example:
1	2	3	4	5	6	7
24	D	D	D	D	D	8
23	D	T	T	T	D	9
22	D	T	B	T	D	10
21	D	T	T	T	D	11
20	D	D	D	D	D	12
19	18	17	16	15	14	13

Each of the two players starts with a score of 501 and they take turns to throw a dart – one throw for each player.
The score for each turn is deducted from the player’s total score. The first player who reduces their score to zero or
less wins the game.
You are going to receive the information for every throw on a separate line. The coordinate information of a hit will
 be in the format: "({row}, {column})".
•	If a player hits outside the dartboard, he does not score any points.
•	If a player hits a number, it is deducted from his total.
•	If a player hits a "D" the sum of the 4 corresponding numbers per column and row is doubled and then deducted
from his total.
•	If a player hits a "T" the sum of the 4 corresponding numbers per column and row is tripled and then deducted
from his total.
•	"B" is the bullseye. If a player hits it, he wins the game, and the program ends.
For example, if Peter hits position with coordinates (2, 1), he wins (23 + 2 + 9 + 18) * 2 = 104 points and they
 are deducted from his total.
Your job is to find who won the game and with how many turns.
Input
•	The name of the first player and the name of the second player, separated by ", "
•	7 lines – the dartboard (separated by single space)
•	On the next lines - the coordinates in the format: "({row}, {column})"
Output
•	You should print only one line containing the winner and his count of throws:
"{name} won the game with {count_turns} throws!"
Constrains
•	There will always be exactly 7 lines
•	There will always be a winner
•	The points will be in range [1, 24]
•	The coordinates will be in range [0, 100]

"""
from collections import deque

DASHBOARD_SIZE = 7


def check_if_in_range(dashboard_size, row, col):
    if row in range(dashboard_size) and col in range(dashboard_size):
        return True
    return False


def hit_letter(dashboard, row, col):
    score_for_hit = 0
    directions = {
        "left": (0, -1),
        "right": (0, 1),
        "down": (1, 0),
        "up": (-1, 0)
    }
    for current_direction, positions in directions.items():
        r, c = positions
        current_row = row + r
        current_col = col + c
        while current_row in range(DASHBOARD_SIZE) and current_col in range(DASHBOARD_SIZE):
            if dashboard[current_row][current_col].isdigit():
                score_for_hit += int(dashboard[current_row][current_col])
                break
            current_row += r
            current_col += c
    return score_for_hit


winner = ''
players = deque(input().split(', '))
dashboard = [input().split() for r in range(DASHBOARD_SIZE)]
players_score = deque([501, 501])
throws = deque([0, 0])
while True:
    scores = 0
    current_player = players[0]
    current_player_score = players_score[0]
    current_throw = throws[0]
    current_throw += 1
    players.append(players.popleft())
    players_score.append(players_score.popleft())
    throws.append(throws.popleft())
    data = input().split(', ')
    hit = (int(data[0][1:]), int(data[1][:-1]))
    row, col = hit
    if check_if_in_range(DASHBOARD_SIZE, row, col):
        if dashboard[row][col] == "D":
            scores = hit_letter(dashboard, row, col)
            scores *= 2
        elif dashboard[row][col] == "T":
            scores = hit_letter(dashboard, row, col)
            scores *= 3
        elif dashboard[row][col] == 'B':
            winner = current_player
            break
        else:
            scores = int(dashboard[row][col])
    current_player_score -= scores
    if current_player_score <= 0:
        break
    players_score[1] = current_player_score
    throws[1] = current_throw
print(f"{current_player} won the game with {current_throw} throws!")
