"""You are given an array with integers. Write a program to modify the elements after receiving the following commands:
•	"swap {index1} {index2}" takes two elements and swap their places.
•	"multiply {index1} {index2}" takes element at the 1st index and multiply it with the element at 2nd index.
Save the product at the 1st index.
•	"decrease" decreases all elements in the array with 1.
Input
On the first input line, you will be given the initial array values separated by a single space.
On the next lines you will receive commands until you receive the command "end". The commands are as follow:
•	"swap {index1} {index2}"
•	"multiply {index1} {index2}"
•	"decrease"
Output
The output should be printed on the console and consist of elements of the modified array – separated by a comma
and a single space ", ".
"""

numbers = [int(i) for i in input().split()]


def command_swap(numbers: list, index1: int, index2: int):
    numbers[index1], numbers[index2] = numbers[index2], numbers[index1]
    return numbers


def command_multiply(numbers: list, index1: int, multiply: int):
    numbers[index1] = numbers[index1] * numbers[multiply]
    return numbers


def command_decrease(numbers: list):
    for i in range(len(numbers)):
        numbers[i] -= 1

    return numbers


command = input()
while command != "end":
    command = command.split()
    if command[0] == "swap":
        first_index = int(command[1])
        second_index = int(command[2])
        command_swap(numbers, first_index, second_index)
    elif command[0] == "multiply":
        first_index = int(command[1])
        multiply = int(command[2])
        command_multiply(numbers, first_index, multiply)

    elif command[0] == "decrease":
        command_decrease(numbers)
    command = input()


numbers = [str(i) for i in numbers]
print(*numbers, sep=', ')
