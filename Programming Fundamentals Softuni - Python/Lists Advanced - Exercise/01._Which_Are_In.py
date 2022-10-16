string_for_search = input().split(', ')
string = input().split(', ')
result = []
for word in string_for_search:
    for n in string:
        if word in n:
            result.append(word)
            break
print(result)