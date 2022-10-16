students = int(input())
fail_students = 0
between_3_4 = 0
between_4_5 = 0
top_students = 0
sum_evaluates = 0
for i in range(1, students+1):
    evaluates = float(input())
    sum_evaluates += evaluates
    if 2 <= evaluates <= 2.99:
        fail_students += 1
    elif 2.99 < evaluates <= 3.99:
        between_3_4 += 1
    elif 3.99 < evaluates <= 4.99:
        between_4_5 += 1
    elif evaluates > 4.99:
        top_students += 1
top_students_percentage = ('% .2f' % (top_students / students * 100))
fail_students_percentage = ('%.2f' % (fail_students / students * 100))
between_3_4_percentage = ('%.2f' % (between_3_4 / students * 100))
between_4_5_percentage = ('%.2f' % (between_4_5 / students * 100))
avarage_evaluates = ('%.2f' % (sum_evaluates / students))
print(f'Top students:{top_students_percentage}%')
print(f'Between 4.00 and 4.99: {between_4_5_percentage}%')
print(f'Between 3.00 and 3.99: {between_3_4_percentage}%')
print(f'Fail: {fail_students_percentage}%')
print(f'Average: {avarage_evaluates}')
