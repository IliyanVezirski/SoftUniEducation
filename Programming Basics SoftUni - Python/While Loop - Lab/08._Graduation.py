name = input()
evaluation = float(input())
counter = 0
two_counter = 0
evaluation_sum = 0
graduated = True
while counter <= 12 or evaluation > 4:
    evaluation_sum += evaluation
    counter += 1
    if evaluation < 4:
        two_counter += 1
        if two_counter == 2:
            counter -= 1
            print(f'{name} has been excluded at {counter} grade')
            graduated = False
            break
    if counter == 12:
        break
    evaluation = float(input())

average_evaluation = ('%.2f' % (evaluation_sum / counter))

if graduated:
    print(f'{name} graduated. Average grade: {average_evaluation}')

