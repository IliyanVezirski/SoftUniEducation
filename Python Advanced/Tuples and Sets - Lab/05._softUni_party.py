len_of_student_list = int(input())

student_list = set()
for _ in range(len_of_student_list):
    student = input()
    student_list.add(student)

student_to_come = input()

while student_to_come != "END":
    if student_to_come in student_list:
        student_list.remove(student_to_come)
    student_to_come = input()
print(len(student_list))
print('\n'.join(sorted(student_list, key=lambda x: (x.isdigit(), x))))
