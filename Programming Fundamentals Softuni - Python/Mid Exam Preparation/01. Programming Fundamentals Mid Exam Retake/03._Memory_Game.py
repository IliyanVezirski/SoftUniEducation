""""Write a program that recreates the Memory game.
On the first line, you will receive a sequence of elements. Each element in the sequence will have a twin.
Until the player receives "end" from the console, you will receive strings with two integers separated by a space, representing the indexes of elements in the sequence.
If the player tries to cheat and enters two equal indexes or indexes which are out of bounds of the sequence, you should add two matching elements at the middle of the sequence in the following format:
"-{number of moves until now}a"
Then print this message on the console:
"Invalid input! Adding additional elements to the board"
Input
•	On the first line, you will receive a sequence of elements
•	On the following lines, you will receive integers until the command "end"
Output
•	Every time the player hit two matching elements, you should remove them from the sequence
and print on the console the following message:
"Congrats! You have found matching elements - ${element}!"
•	If the player hit two different elements, you should print on the console the following message:
"Try again!"
•	If the player hit all matching elements before he receives "end" from the console,
you should print on the console the following message:
"You have won in {number of moves until now} turns!"
•	If the player receives "end" before he hits all matching elements,
you should print on the console the following message:
"Sorry you lose :(
{the current sequence's state}"
Constraints
•	All elements in the sequence will always have a matching element.
"""

sequence = input().split()
targets_indexes = input()
games_counter = 0
won_game = True
while targets_indexes != "end":
    targets_indexes = targets_indexes.split()
    first_index = int(targets_indexes[0])
    second_index = int(targets_indexes[1])
    games_counter += 1
    if first_index != second_index and 0 <= first_index < len(sequence) and 0 <= second_index < len(sequence):
        if sequence[first_index] == sequence[second_index]:
            element_to_remove = sequence[first_index]
            print(f"Congrats! You have found matching elements - {element_to_remove}!")
            sequence.remove(element_to_remove)
            sequence.remove(element_to_remove)

        else:
            print(f"Try again!")
    else:
        print(f"Invalid input! Adding additional elements to the board")
        index_half = len(sequence) // 2
        sequence.insert(index_half, '-'+str(games_counter)+'a')
        sequence.insert(index_half, '-'+str(games_counter)+'a')
    if sequence == []:
        print(f'You have won in {games_counter} turns!')
        break
    targets_indexes = input()

if sequence != []:
    print("Sorry you lose :(")
    print(' '.join(sequence))