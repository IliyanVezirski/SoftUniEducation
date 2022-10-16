groups = int(input())
musala = 0
kilimandjaro = 0
monblan = 0
k2 = 0
everes = 0
total_people = 0
for group in range(groups):
    people = int(input())
    if people <= 5 :
        musala += people
        total_people += people
    elif 5 < people <= 12:
        monblan += people
        total_people += people
    elif 13 <= people <= 25:
        kilimandjaro += people
        total_people += people
    elif 26 <= people <= 40:
        k2 += people
        total_people += people
    elif people >= 41:
        everes += people
        total_people += people
percentage_musala = musala / total_people * 100
percentage_monblan = monblan / total_people * 100
percentage_kilimandjaro = kilimandjaro / total_people * 100
percentage_k2 = k2 / total_people * 100
percentage_everes = everes / total_people * 100
print(f'{percentage_musala:.2f}%')
print(f'{percentage_monblan:.2f}%')
print(f'{percentage_kilimandjaro:.2f}%')
print(f'{percentage_k2:.2f}%')
print(f'{percentage_everes:.2f}%')