employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
students = int(input())
students_per_hour =  employee_1 + employee_2 + employee_3
hour = 0
while students > 0:
    hour += 1
    if hour % 4 == 0:
        hour += 1
    students -= students_per_hour
print(f"Time needed: {hour}h.")