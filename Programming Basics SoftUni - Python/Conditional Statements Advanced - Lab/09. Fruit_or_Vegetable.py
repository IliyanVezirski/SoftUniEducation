name = input()
type_name = ''
if name == 'banana' or name == 'apple' or name == 'kiwi' or name == 'cherry' or name == 'lemon' or name == 'grapes':
    type_name = 'fruit'
elif name == 'tomato' or name == 'cucumber' or name == 'pepper' or name == 'carrot':
    type_name = 'vegetable'
else:
    type_name = 'unknown'
print(type_name)