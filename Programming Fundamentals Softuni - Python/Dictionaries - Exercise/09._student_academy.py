grades = {}

students = int(input())

for count in range(students):
    student = input()
    grade = float(input())
    if student not in grades:
        grades[student] = [grade]
    else:
        student_grades = grades[student]
        student_grades.append(grade)
        grades[student] = student_grades
grades_of_best_students = {}
for k, v in grades.items():
    average_grade = sum(v)/len(v)
    if average_grade < 4.5:
        continue
    else:
        grades_of_best_students[k] = average_grade
for k, v in grades_of_best_students.items():
    print(f"{k} -> {v:.2f}")