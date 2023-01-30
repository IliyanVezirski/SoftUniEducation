"""
A chessboard has 8 rows and 8 columns. Rows, also called ranks, are marked from number 1 to 8, and columns are marked
 from A to H. We have a total of 64 squares. Each square is represented by a combination of letters and a number
  (a1, b1, c1, etc.). In this problem colors of the board will be ignored.
We will play the game with two pawns, white (w) and black (b), where they can:
•	Only move forward in a straight line:
	White (w) moves from the 1st rank to the 8th rank direction.
	Black (b) moves from 8th rank to the 1st rank direction.
•	Can move only 1 square at a time.
•	Can capture another pawn in from of them only diagonally:

When a pawn reaches the last rank (for the white one - this is the 8th rank, and for the black one - this is the 1st
 rank), can be promoted to a queen.
Two pawns (w and b) will be placed on two random squares of the bord. The first move is always made by the white
pawn (w), then black moves (b), then white (w) again, and so on.


Some rules apply when moving paws:
•	If the two pawns interact diagonally, the player, in turn, must capture the opponent's pawn.
When a pawn captures another pawn, the game is over.
•	If no capture is possible, the pawns keep on moving until one of them reaches the last rank.
Input
•	On 8 lines, you will receive each row with its 8 columns, each element separated by a single space:
o	Empty positions are marked with "-".
o	White pawn is marked with "w"
o	Black pawn is marked with "b"
Output
Print either one of the following:
•	If a pawn captures the other, print:
o	"Game over! {White/Black} win, capture on {square}."
•	If a pawn reaches the last rank, print:
o	"Game over! {White/Black} pawn is promoted to a queen at {square}."
Constraints
•	The input will always be valid.
•	The matrix will always be 8x8.
•	There will be no case where two pawns are placed on the same square.
•	There will be no case where two pawns are placed on the same column.
•	There will be no case where black/white will be placed on the last rank.

"""

boards_col_names = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h'
}

boards_row_names = {
    0: '8',
    1: '7',
    2: '6',
    3: '5',
    4: '4',
    5: '3',
    6: '2',
    7: '1'
}
from collections import deque

directions_for_white = (-1, 0)
directions_for_black = (+1, 0)


def in_range(row, col, size):
    if row in range(size) and col in range(size):
        return True
    return False


def check_white_diagonals(chessboard: list, white_position: tuple):
    if in_range(white_position[0] - 1, white_position[1] - 1, 8):
        if chessboard[white_position[0] - 1][white_position[1] - 1] == "b":
            return True
    if in_range(white_position[0] - 1, white_position[1] + 1, 8):
        if chessboard[white_position[0] - 1][white_position[1] + 1] == 'b':
            return True
    return False


def check_black_diagonals(chessboard: list, black_position: tuple):
    if in_range(black_position[0] + 1, black_position[1] + 1, 8):
        if chessboard[black_position[0] + 1][black_position[1] + 1] == 'w':
            return True
    if in_range(black_position[0] + 1, black_position[1] - 1, 8):
        if chessboard[black_position[0] + 1][black_position[1] - 1] == "w":
            return True
    return False


chessboard_size = 8
white_position = tuple()
black_position = tuple()
players_turn = deque(['w', 'b'])
chessboard = []
for row in range(chessboard_size):
    chessboard.append(input().split())
    for col in range(chessboard_size):
        if chessboard[row][col] == 'w':
            white_position = (row, col)
        elif chessboard[row][col] == 'b':
            black_position = (row, col)
queen = False
winner_position = ''
winner = ''
while True:
    current_player = players_turn.popleft()
    players_turn.append(current_player)
    if current_player == 'w':
        if check_white_diagonals(chessboard, white_position):
            winner = 'White'
            winner_position = boards_col_names[black_position[1]] + boards_row_names[black_position[0]]
            break
        new_position = white_position[0] + directions_for_white[0], white_position[1] + directions_for_white[1]
        if new_position[0] == 0:
            winner_position = boards_col_names[new_position[1]] + boards_row_names[new_position[0]]
            winner = 'White'
            queen = True
            break
        chessboard[new_position[0]][new_position[1]] = 'w'
        chessboard[white_position[0]][white_position[1]] = '-'
        white_position = new_position
    else:
        if check_black_diagonals(chessboard, black_position):
            winner_position = boards_col_names[white_position[1]] + boards_row_names[white_position[0]]
            winner = 'Black'
            break
        new_position = black_position[0] + directions_for_black[0], black_position[1] + directions_for_black[1]
        if new_position[0] == chessboard_size - 1:
            winner_position = boards_col_names[new_position[1]] + boards_row_names[new_position[0]]
            winner = "Black"
            queen = True
            break
        chessboard[new_position[0]][new_position[1]] = 'b'
        chessboard[black_position[0]][black_position[1]] = '-'
        black_position = new_position
if queen:
    print(f'Game over! {winner} pawn is promoted to a queen at {winner_position}.')
else:
    print(f'Game over! {winner} win, capture on {winner_position}.')
