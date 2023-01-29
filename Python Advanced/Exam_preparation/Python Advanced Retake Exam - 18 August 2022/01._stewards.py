"""
"It's only when you are flying above that you realize how incredible the Earth really is."
As you know, stewards are needed for every single flight. Today you will be that one steward, and you will be assisting
the passengers in finding their seats.
You will be given a sequence of 6 seats - every seat is a mix of a number and a letter in the format "{number}{letter}".
You will also be given two more sequences of numbers only.
First, you have to take the first number of the first sequence and the last number of the second sequence. Next, take
 the sum of those two numbers and find its ASCII character.
•	Compare each of the two taken numbers and the found character with the seats. If you find a match, the passenger
 is seated, and the seat is considered taken. Remove both numbers from their sequences.
•	If there is no equality, the two numbers should be returned at the end of their sequences (first becomes last,
last becomes first).
•	If you match an already taken seat, you should just remove both numbers from their sequences.
Each time you take numbers from the sequences and try to match them, you make one rotation. You should keep track
 of all rotations made.
The program should end under the following circumstances:
•	You have found 3 (three) seat matches
•	You have made a total of 10 rotations
Input
•	On the first line, you will be given a sequence of seats - strings separated by comma and space ", "
•	On the second and the third line, you will be given two more sequences - integers separated by a comma and a space
 ", "
Output
When the program ends, print the following on two different lines:
o	Seat matches: {matches separated by comma and space}
o	Rotations count: {total rotations made}
Constraints
•	All integers will be in the range [1, 100]
•	All letters will be in the range [A-Z]
•	You will never run out of numbers in your sequences before the program ends
•	You will never have more than one match at a time

"""
from collections import deque
taken_seats = []
seats = input().split(', ')
first_sequence = deque(int(i) for i in input().split(', '))
second_sequence = deque(int(i) for i in input().split(', '))
rotation = 0
while first_sequence and second_sequence:
    rotation += 1
    founded = False
    current_first = first_sequence.popleft()
    current_second = second_sequence.pop()
    sum_of_first_and_second = current_second + current_first
    current_char = chr(sum_of_first_and_second)
    first_check = f'{current_first}{current_char}'
    second_check = f'{current_second}{current_char}'
    for seat in seats:
        if seat == first_check or seat == second_check:
            taken_seats.append(seat)
            founded = True
            break
    if not founded:
        for seat in taken_seats:
            if first_check == seat or second_check == seat:
                founded = True
                break
    if not founded:
        first_sequence.append(current_first)
        second_sequence.appendleft(current_second)
    if len(taken_seats) == 3:
        break
    if rotation == 10:
        break
print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotation}")