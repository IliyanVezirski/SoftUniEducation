string = (input())
result = [i for i in string if i != 'a' and i != 'o' and i != 'u' and i != 'e' and i != 'i']
print(*result, sep='')