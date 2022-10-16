cards = input().split()
number_of_cards = int(input())
half_deck = len(cards) // 2
left_half = cards[0:half_deck]
right_half = cards[half_deck:]
shuffled_deck = []
for shuffle in range(number_of_cards):
    shuffled_deck = []
    for shuffle2 in range(half_deck):
        shuffled_deck.append(left_half[shuffle2])
        shuffled_deck.append(right_half[shuffle2])
    left_half = shuffled_deck[0:half_deck]
    right_half = shuffled_deck[half_deck:]

print(shuffled_deck)