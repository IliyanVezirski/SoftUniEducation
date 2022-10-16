people = [int(n) for n in input().split()]
happines_index = int(input())
happynes = [i * happines_index for i in people]

happy_value = sum(happynes) / len(happynes)
happy_people = [i for i in happynes if i >= happy_value]
sad_people = [n for n in happynes if n  < happy_value]
if len(happy_people) >= len(people)/2:
    print(f'Score: {len(happy_people)}/{len(people)}. Employees are happy!')
else:
    print(f'Score: {len(happy_people)}/{len(people)}. Employees are not happy!')