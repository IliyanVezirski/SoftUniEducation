movie_name = ''
count_standard_for_movie = 0
count_student_for_movie = 0
count_kid_for_movie = 0
total_count_for_movie = 0
total_count = 0
total_count_kids = 0
total_count_student = 0
total_count_standard = 0
total_free_spaces = 0
while movie_name != "Finish":
    count_standard_for_movie = 0
    count_student_for_movie = 0
    count_kid_for_movie = 0
    total_count_for_movie = 0
    movie_name = input()
    if movie_name == 'Finish':
        break
    free_space = int(input())
    total_free_spaces += free_space
    for i in range(1, free_space + 1):
        type_ticket = input()
        if type_ticket == 'standard':
            count_standard_for_movie += 1
            total_count_for_movie += 1
            total_count += 1
            total_count_standard += 1
        elif type_ticket == 'kid':
            count_kid_for_movie += 1
            total_count_for_movie += 1
            total_count += 1
            total_count_kids +=1
        elif type_ticket == 'student':
            count_student_for_movie += 1
            total_count_for_movie += 1
            total_count += 1
            total_count_student += 1
        if type_ticket == 'End':
            break
    space_full = (total_count_for_movie) / free_space * 100
    print(f'{movie_name} - {space_full:.2f}% full.')
percentage_kids = total_count_kids / total_count * 100
percentage_students = total_count_student / total_count * 100
percentage_standard = total_count_standard / total_count * 100
print(f'Total tickets: {total_count}')
print(f'{percentage_students:.2f}% student tickets.')
print(f'{percentage_standard:.2f}% standard tickets.')
print(f'{percentage_kids:.2f}% kids tickets.')