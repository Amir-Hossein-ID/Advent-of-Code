s = input()

v = {(0,0)}
last1 = 0,0
last2 = 0,0
turn = True

for i in s:
    if turn:
        last = last1
    else:
        last = last2
    if i == 'v':
        last = last[0], last[1] - 1
    elif i == '^':
        last = last[0], last[1] + 1
    elif i == '>':
        last = last[0] + 1, last[1]
    else:
        last = last[0] - 1, last[1]
    if turn:
        last1 = last
    else:
        last2 = last
    turn = not turn
    v.add(last)

print(len(v))
