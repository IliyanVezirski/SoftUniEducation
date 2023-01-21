board_size = int(input())
board = [[i for i in input()] for r in range(board_size)]

knight_moves = [
    (-1, +2),
    (-2, +1),
    (-2, -1),
    (-1, -2),
    (+1, -2),
    (+2, -1),
    (+2, +1),
    (+1, +2)
]
counter = 0
while True:
    knight_positions = []
    knight_hits = []
    for r in range(board_size):
        for c in range(board_size):
            if board[r][c] == 'K':
                knight_positions.append((r, c))
    for current_knight in knight_positions:
        counter_for_k = 0
        for position in knight_moves:
            looked_knight = (current_knight[0] + position[0], current_knight[1] + position[1])
            if looked_knight[0] in range(board_size) and looked_knight[1] in range(board_size):
                if board[looked_knight[0]][looked_knight[1]] == "K":
                    counter_for_k += 1

        knight_hits.append(counter_for_k)
    best_fighter = knight_positions[knight_hits.index(max(knight_hits))]
    board[best_fighter[0]][best_fighter[1]] = '0'
    if sum(knight_hits) == 0:
         break
    counter += 1
print(counter)