poor_grades = int(input())
counter = 0
poor_score = 0
sum_score = 0
name_problems = ''
last_problem = ''
while name_problems != 'Enough':
    name_problems = input()
    if name_problems == 'Enough':
        break
    score = float(input())
    last_problem = name_problems
    sum_score += score
    if score <= 4:
        poor_score += 1
        if poor_score == poor_grades:
            print(f'You need a break, {poor_score} poor grades.')
            break
    counter += 1
average_score = sum_score / counter
if name_problems == 'Enough':
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {counter}')
    print(f'Last problem: {last_problem}')