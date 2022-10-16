budget = int(input())
bought = input()
while bought != "End":
    budget -= int(bought)
    if budget < 0:
        print("You went in overdraft!")
        break
    bought = input()
    if bought == "End":
        break
if budget >= 0:
    print('You bought everything needed.')