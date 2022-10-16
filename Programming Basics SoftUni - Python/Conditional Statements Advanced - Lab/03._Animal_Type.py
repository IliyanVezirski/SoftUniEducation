animal = input()
if animal == 'dog':
    animal_name = 'mammal'
elif animal == 'snake' or animal == 'tortoise' or animal == 'crocodile':
    animal_name = 'reptile'
else:
    animal_name = 'unknown'
print( animal_name)