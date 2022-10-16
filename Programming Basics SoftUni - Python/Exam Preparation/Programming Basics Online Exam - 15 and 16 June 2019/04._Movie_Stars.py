budget = float(input())
actor = input()
total = 0
diff = 0
while actor != 'ACTION':
    if diff < 0:
        break
    actor_len = len(actor)
    if actor_len > 15:
        price = diff * 0.20
    else:
        price = float(input())
    total += price
    diff = budget - total
    actor = input()
if diff >= 0:
    print(f"We are left with {diff:.2f} leva.")
else:
    print(f'We need {abs(diff):.2f} leva for our actors.')
