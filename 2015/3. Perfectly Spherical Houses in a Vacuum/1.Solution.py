s = input()

v = {(0,0)}
last = 0,0

for i in s:
    if i == 'v':
        last = last[0], last[1] - 1
    elif i == '^':
        last = last[0], last[1] + 1
    elif i == '>':
        last = last[0] + 1, last[1]
    else:
        last = last[0] - 1, last[1]
    v.add(last)

print(len(v))
