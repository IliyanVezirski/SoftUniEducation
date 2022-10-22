students = input()
course = {}
while True:
    if ":" not in students:
        course_type = students.split('_')
        course_type = ' '.join(course_type)
        break
    students = students.split(':')
    course[students[1]] = [students[0], students[2]]
    students = input()
for k, v in course.items():
    if v[1] == course_type:
        print(f"{v[0]} - {k}")
