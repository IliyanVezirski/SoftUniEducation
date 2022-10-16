def grades_condition():
    grave = float(input())
    grave_condition = ''
    if grave >= 2 and grave <= 2.99:
        grave_condition = 'Fail'
    elif grave >= 3 and grave <= 3.49:
        grave_condition = "Poor"
    elif grave >= 3.5 and grave <= 4.49:
        grave_condition = "Good"
    elif grave >= 4.5 and grave <= 5.49:
        grave_condition = "Very Good"
    elif grave >= 5.5 and grave <= 6:
        grave_condition = "Excellent"
    return grave_condition


print(grades_condition())