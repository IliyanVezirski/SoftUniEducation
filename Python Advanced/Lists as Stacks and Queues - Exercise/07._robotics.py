from collections import deque

robots = input().split(';')
robots = deque(robots)
time = [int(i) for i in input().split(':')]
time[0] = time[0] * 60
time[1] = time[0] + time[1]
time_in_seconds = time[1] * 60 + time[2]
print(time_in_seconds)
tasks = deque()
task = input()
while task != "End":
    tasks.add(task)
    time_in_seconds += 1
    if robots:
        robot_to_take_task = robots.popleft()
        time_needed = int(robot_to_take_task.split('-')[1])
        busy_time.append(time_needed)
