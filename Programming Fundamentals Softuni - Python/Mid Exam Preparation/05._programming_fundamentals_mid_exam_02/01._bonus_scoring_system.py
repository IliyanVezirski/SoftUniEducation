import math

students = int(input())
lectures = int(input())
additional_bonus = int(input())
best_students = 0
total_bonus = 0
lectures_of_best_student = 0
for student in range(students):
    attendace = int(input())
    total_bonus = attendace / lectures * (5 + additional_bonus)
    if total_bonus > best_students:
        best_students = total_bonus
        lectures_of_best_student = attendace
print(f"Max Bonus: {round(best_students)}.")
print(f"The student has attended {lectures_of_best_student} lectures.")
