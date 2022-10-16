"""Write a program to read a sequence of integers and find and print the top 5 numbers greater than the average value in the sequence, sorted in descending order.
Input
•	Read from the console a single line holding space-separated integers.
Output
•	Print the above-described numbers on a single line, space-separated.
•	If less than 5 numbers hold the property mentioned above, print less than 5 numbers.
•	Print "No" if no numbers hold the above property.
Constraints
•	All input numbers are integers in the range [-1 000 000 … 1 000 000].
•	The count of numbers is in the range [1…10 000].
"""

sequence_of_numbers = [int(i) for i in input().split()]
average = sum(sequence_of_numbers) / len(sequence_of_numbers)
sequence_of_numbers = list(sorted(sequence_of_numbers))
greater_numbers_then_average = []
for i in sequence_of_numbers[::-1]:
    if len(greater_numbers_then_average) == 5:
        break
    if i > average:
        greater_numbers_then_average.append(i)


if greater_numbers_then_average == []:
    print(f'No')
else:
    print(*greater_numbers_then_average, sep=' ')
