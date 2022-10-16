numbers = input().split()
numbers_to_remove = int(input())
numbers_int = []
numbers_for_remove = []
numbers_to_compare = []
for i in range(len(numbers)):
    numbers_int.append(int(numbers[i]))
    numbers_to_compare.append(int(numbers[i]))
numbers_int.sort()
for n in range(numbers_to_remove):
    numbers_for_remove.append(numbers_int[n])
for j in numbers_for_remove:
    for l in numbers_to_compare:
        if j == l:
            numbers_to_compare.remove(j)

word_to_print = str(numbers_to_compare)
word_to_print = word_to_print.replace("]", "")
word_to_print = word_to_print.replace("[", "")
print(word_to_print)
