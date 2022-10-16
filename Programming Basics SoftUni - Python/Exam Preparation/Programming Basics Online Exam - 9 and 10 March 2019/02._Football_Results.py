result_from_first_match = input()
result_from_second_match = input()
result_from_third_match = input()
first_match_host_goals = int(result_from_first_match[0])
first_match_guest_goals = int(result_from_first_match[2])
second_match_host_goals = int(result_from_second_match[0])
second_match_guest_goals = int(result_from_second_match[2])
third_match_host_goals = int(result_from_third_match[0])
third_match_guest_goals = int(result_from_third_match[2])

winner_counter = 0
loses_counter = 0
drawn_counter = 0
if first_match_host_goals > first_match_guest_goals:
    winner_counter += 1
elif first_match_host_goals == first_match_guest_goals:
    drawn_counter += 1
elif first_match_host_goals < first_match_guest_goals:
    loses_counter += 1
if second_match_host_goals > second_match_guest_goals:
    winner_counter += 1
elif second_match_host_goals == second_match_guest_goals:
    drawn_counter += 1
elif second_match_host_goals < second_match_guest_goals:
    loses_counter += 1
if third_match_host_goals > third_match_guest_goals:
    winner_counter += 1
elif third_match_host_goals == third_match_guest_goals:
    drawn_counter += 1
elif third_match_host_goals < third_match_guest_goals:
    loses_counter += 1
print(f'Team won {winner_counter} games.')
print(f'Team lost {loses_counter} games.')
print(f'Drawn games: {drawn_counter}')