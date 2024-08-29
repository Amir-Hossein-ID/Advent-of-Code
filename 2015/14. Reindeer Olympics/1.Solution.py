fastest = 0
race_end = 2503

for i in range(9): # no of lines of input
    new = input().split()
    distance = 0
    speed, run_time, rest_time = int(new[3]), int(new[6]), int(new[-2])
    distance = race_end // (run_time + rest_time) * speed * run_time
    left = race_end % (run_time + rest_time)
    distance += speed * left if left <= run_time else run_time * speed

    if distance > fastest:
        fastest = distance

print(fastest)
