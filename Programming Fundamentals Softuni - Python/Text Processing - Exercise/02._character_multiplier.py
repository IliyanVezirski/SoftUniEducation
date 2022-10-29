strings = input().split()

str1 = strings[0]
str2 = strings[1]

result = 0
word = ''
if len(str1) >= len(str2):
    while word != str2:
        for i in range(len(str2)):
            result += ord(str2[i]) * ord(str1[i])
            word += str2[i]
        for i in str1[len(str2):]:
            result += ord(i)
else:
    while word != str1:
        for i in range(len(str1)):
            result += ord(str1[i]) * ord(str2[i])
            word += str1[i]
        for i in str2[len(str1):]:
            result += ord(i)
print(result)
