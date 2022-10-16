capacity = int(input())
people = input()
sum_people = 0
total = 0
while people != 'Movie time!':
    peoples = int(people)
    sum_people += peoples
    total_for_peoples = 0
    if sum_people > capacity:
        print(f'The cinema is full.')
        break
    if peoples % 3 == 0:
        total_for_peoples = peoples * 5 - 5
    else:
        total_for_peoples = peoples * 5
    total += total_for_peoples
    people = input()
    if people == 'Movie time!':
        break
diff = abs(sum_people - capacity)
if capacity >= sum_people:
    print(f'There are {diff} seats left in the cinema.')
print(f'Cinema income - {total} lv.')