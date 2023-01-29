def age_assignment(*names, **kwargs):
    result = []
    for letter, age in kwargs.items():
        for name in names:
            if name[0] == letter:
                result.append(f"{name} is {age} years old.")
    result = list(sorted(result, key=lambda x: x))
    return '\n'.join(result)
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
print(age_assignment("Peter", "George", G=26, P=19))