"""
Tom and Jerry decided to play a game together. The game is a maze of which they need to find a way out. Monitor their
moves closely and find out who the winner will be!
First, you will be given the names "Tom" and "Jerry", separated by a comma and a space ", ". The order in which they
are received determines the order in which they will take turns. The first player starts first.
Next, you will be given a matrix with 6 rows and 6 columns representing the maze board. It consists of:
•	Only one Exit - marked with the "E" letter
•	Trap (one, many, or none) - marked with the "T" letter
•	Wall (one, many, or none) - marked with the "W" letter
•	Empty positions will be marked with "."
In the beginning, Tom and Jerry are outside the board. On each line, after the matrix is given, you will
 be receiving coordinates for each of the players. They will be taking turns and stepping on different positions
  on the board until one of them find the Exit or falls into a Trap. Here are the rules:
•	If a player hits the letter "E", he escapes the maze and wins the game.
o	Print "{player} found the Exit and wins the game!" and end the program.
•	If the letter "T" is hit, the player falls into a Trap, the game ends, and his opponent wins automatically.
o	Print "{player} is out of the game! The winner is {winner}." and end the program.
•	If the letter "W" is hit, the player hits a wall, and he needs to rest. The player's next move is ignored.
o	Print "{player} hits a wall and needs to rest."
•	If a player steps on an empty position ".", nothing happens.
•	Both players can step in the same position at the same time.
Input
•	On the first line, you will receive "Tom" and "Jerry" separated by ", ". The first player starts first.
•	On the following 6 lines, you will receive the maze board (elements will be separated by a space)
•	On the following lines, you will be receiving coordinates in the format: "({row}, {column})"
Output
•	You should print the output as described above.
•	The input coordinates will always be valid.

"""
from collections import deque

players = deque(input().split(', '))
tom_traps = 0
jerry_traps = 0
tom_wall = 0
jerry_wall = 0
field_size = 6
field = [input().split() for i in range(field_size)]
while True:
    player_turn = players.popleft()
    players.append(player_turn)
    position_to_play = input().split(', ')
    position_to_play = (int(position_to_play[0][1]), int(position_to_play[1][0]))
    if player_turn == "Tom" and tom_wall > 0:
        tom_wall -= 1
        continue
    elif player_turn == "Jerry" and jerry_wall > 0:
        jerry_wall -= 1
        continue
    if field[position_to_play[0]][position_to_play[1]] == "E":
        print(f"{player_turn} found the Exit and wins the game!")
        break
    elif field[position_to_play[0]][position_to_play[1]] == "T":
        print(f"{player_turn} is out of the game! The winner is {players[0]}.")
        break
    elif field[position_to_play[0]][position_to_play[1]] == "W":
        if player_turn == "Tom":
            tom_wall += 1
        else:
            jerry_wall += 1
        print(f"{player_turn} hits a wall and needs to rest.")
