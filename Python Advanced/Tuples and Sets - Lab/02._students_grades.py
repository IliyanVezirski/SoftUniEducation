students_number = int(input())
students = {}
for _ in range(students_number):
    current_student = tuple(input().split())
    if current_student[0] not in students:
        students[current_student[0]] = []
    students[current_student[0]].append(float(current_student[1]))
students_to_print = {}

for student, grade in students.items():
    for current_grade in grade:
        if student not in students_to_print:
            students_to_print[student] = []
        students_to_print[student].append(f'{current_grade:.2f}')
for student, grade in students.items():
    print(f"{student} -> {' '.join(students_to_print[student])} (avg: {sum(grade)/ len(grade):.2f})")