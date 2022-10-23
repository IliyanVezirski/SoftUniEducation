course = {}


course_student = input()

while course_student != "end":
    course_student = course_student.split(' : ')
    lesson = course_student[0]
    name = course_student[1]
    if lesson in course:
        lesson_list = course[lesson]
        lesson_list.append(name)
        course[lesson] = lesson_list
    else:
        course[lesson] = [name]
    course_student = input()
for k in course:
    print(f"{k}: {len(course[k])}")
    for v in course[k]:
        print(f"-- {v}")

