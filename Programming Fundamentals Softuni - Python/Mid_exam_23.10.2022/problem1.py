needed_experience = float(input())
battles = int(input())
experience = 0
won = False
for i in range(1, battles + 1):
    experience_gained = float(input())
    if i % 3 == 0:
        experience_gained *= 1.15
    if i % 5 == 0:
        experience_gained *= 0.9
    if i % 15 == 0:
        experience_gained *= 1.05
    experience += experience_gained
    if experience >= needed_experience:
        print(f"Player successfully collected his needed experience for {i} battles.")
        won = True
        break
if not won:
    print(f"Player was not able to collect the needed experience, {needed_experience - experience:.2f} more needed.")