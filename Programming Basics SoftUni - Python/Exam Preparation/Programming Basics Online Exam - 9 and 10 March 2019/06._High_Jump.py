desired_high = int(input())
start_high = desired_high - 30
successful_jumps = 0
unsuccessful_jumps = 0
success = True
jumps_counter = 0
while True:
    jump = int(input())
    if jump > start_high:
        successful_jumps += 1
        start_high += 5
        unsuccessful_jumps = 0
        jumps_counter += 1
    else:
        unsuccessful_jumps += 1
        jumps_counter += 1
        if unsuccessful_jumps == 3:
            success = False
            break
    if start_high > desired_high:
        break
if start_high <= desired_high:
    print(f'Tihomir failed at {start_high}cm after {jumps_counter} jumps.')
else:
    print(f'Tihomir succeeded, he jumped over {start_high - 5}cm after {jumps_counter} jumps.')