"""
Write a function words_sorting which receives a different number of words.
Create a dictionary, which will have as keys the words that the function received. For each key,
create a value that is the sum of all ASCII values of that key.
Then, sort the dictionary:
•	By values in descending order, if the sum of all values of the dictionary is odd
•	By keys in ascending order, if the sum of all values of the dictionary is even
Note: Submit only the function in the judge system
Input
•	There will be no input, just any number of words passed to your function
Output
•	The function should return a string in the format "{key} - {value}" for each key and value on a separate lines
Constraints:
•	There will be no case with capital letters.
•	There will be no case with a string consisting of other than letters.

"""


def words_sorting(*args):
    final_result = []
    words = {}
    sum_result = 0
    for word in args:
        result = 0
        for letter in word:
            result += ord(letter)
            sum_result += ord(letter)
        if word not in words:
            words[word] = 0
            words[word] += result
    if sum_result % 2 == 0:
        words = dict(sorted(words.items(), key=lambda x: x[0]))
    else:
        words = dict(sorted(words.items(), key=lambda x: -x[1]))
    for word, points in words.items():
        final_result.append(f"{word} - {str(points)}")

    return '\n'.join(final_result)

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
