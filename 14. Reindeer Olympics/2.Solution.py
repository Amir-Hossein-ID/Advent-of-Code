fastest = 0
race_end = 2503

seconds = [[] for i in range(race_end)]

input_num = 9

for i in range(input_num): # no of lines of input
    new = input().split()
    speed, run_time, rest_time = int(new[3]), int(new[6]), int(new[-2])
    in_run = True
    curr = run_time
    where = 0

    for j in range(race_end):
        if in_run:
            where += speed
            seconds[j].append(where)
        else:
            seconds[j].append(where)
        curr -= 1
        if curr == 0:
            curr = rest_time if in_run else run_time
            in_run = not in_run

points = [0] * input_num
for i in range(race_end):
    ma = max(seconds[i])

    for j in range(input_num):
        if seconds[i][j] == ma:
            points[j] += 1

print(max(points))
