jury = int(input())
presentation = input()
presentation_count = 0
average_evaluation_sum = 0
while presentation != 'Finish':
    presentation_count += 1
    evaluation_sum = 0
    for i in range(jury):
        evaluation = float(input())
        evaluation_sum += evaluation
    average_evaluation = evaluation_sum / jury
    print(f'{presentation} - {average_evaluation:.2f}.')
    average_evaluation_sum += average_evaluation
    presentation = input()
total_average = average_evaluation_sum / presentation_count
print(f"Student's final assessment is {total_average:.2f}.")