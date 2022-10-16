period = int(input())
doctors = 7
patients_sum = 0
doctors_sum = 0
untreated_patients = 0
untreated_patients_for_day = 0
for days in range(1, period+1):
    patients = int(input())
    patients_sum += patients
    doctors_sum += doctors
    untreated_patients_sum = patients_sum - doctors_sum
    treated_patients_sum = patients_sum - untreated_patients_sum
    if days % 3 == 0 and untreated_patients_sum > treated_patients_sum:
        doctors += 1
    untreated_patients_for_day = patients - doctors
    if untreated_patients_for_day < 0:
        untreated_patients_for_day = 0
    untreated_patients += untreated_patients_for_day
treated_patients = patients_sum - untreated_patients
print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')