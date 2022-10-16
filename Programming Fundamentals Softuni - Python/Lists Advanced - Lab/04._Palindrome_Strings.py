palindrome = input().split()
word_to_search = input()
counter = 0
palindrome_word = []
for word in palindrome:
    revers_word = word[::-1]
    if word == revers_word:
        palindrome_word.append(word)
        if word_to_search == word:
            counter += 1

print(palindrome_word)
print(f"Found palindrome {counter} times")