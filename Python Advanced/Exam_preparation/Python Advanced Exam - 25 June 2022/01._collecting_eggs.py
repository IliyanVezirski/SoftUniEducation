"""
Old MacDonald wants to fill some boxes with eggs. But he has a big farm, and he will need some help.
On the first line, you will receive a sequence of numbers, each representing an egg with its size. On the second line
, you will receive another sequence of numbers, each representing a piece of paper with its size.
You should take the first egg and wrap it with the last piece of paper. Then, try to put it in a box with a size of 50.
 Each wrapped-in-a-paper egg fills one box if it fits in it. Your task is to check whether you have filled at least one box.
You should comply with the following conditions:
•	If the egg is not fresh anymore (its size is less than or equal to 0), you need to remove it from the sequence before
 it is wrapped with a piece of paper.
•	If the sum of the egg's size and the paper's size is less than or equal to the box's size (50), put the wrapped egg
 in the box and remove both from the sequences.
o	Otherwise, you cannot fill a box, so remove both the egg and the paper from the sequences without putting them
 in a box.
•	During your work, you noticed that Old MacDonald is superstitious. If the size of an egg is 13 it brings bad luck
to him. You should remove this egg from the sequence before it is wrapped with a piece of paper.
o	Furthermore, each time you take an egg with a size of 13, it will be best to swap the first and last pieces of
paper positions to bring the good luck back to Old MacDonald.
	Note: There will be NO case where there will be just one piece of paper left.
For more clarification see the examples below.
Input
•	In the first line, you will be given a sequence of eggs with their sizes - integers separated by comma and space
 ", " in the range [-100, 100]
•	In the second line, you will be given a sequence of pieces of paper with their sizes - integers separated by comma and
 space ", " in the range [1, 100]
Output
•	On the first line:
o	If you have at least one box filled, print:
	"Great! You filled {total count} boxes."
o	If you couldn't fill any boxes, print:
	"Sorry! You couldn't fill any boxes!"
•	On the following lines, print the eggs left or pieces of paper left if there are any:
o	Eggs left: {left eggs joined by ", "}
o	Pieces of paper left: {left pieces of paper joined by ", "}
Constraints
•	You will always have at least one egg and at least one piece of paper.

"""

from collections import deque

eggs_size = deque(int(i) for i in input().split(', '))
paper_pieces = deque(int(i) for i in input().split(', '))
box_size = 50
filled_box = 0
while eggs_size and paper_pieces:
    current_egg = eggs_size.popleft()
    while current_egg <= 0 or current_egg == 13:
        if current_egg == 13:
            paper_1 = paper_pieces.pop()
            paper = paper_pieces.popleft()
            paper_pieces.appendleft(paper_1)
            paper_pieces.append(paper)
        if eggs_size:
            current_egg = eggs_size.popleft()
        else:
            break
    if current_egg > 0 and current_egg != 13:
        current_paper = paper_pieces.pop()
        current_sum = current_paper + current_egg
        if current_sum <= box_size:
            filled_box += 1
if filled_box > 0:
    print(f"Great! You filled {filled_box} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs_size:
    print(f"Eggs left: {', '.join([str(i) for i in eggs_size])}")
if paper_pieces:
    print(f"Pieces of paper left: {', '.join([str(i) for i in paper_pieces])}")
