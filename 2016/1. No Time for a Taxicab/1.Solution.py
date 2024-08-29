moves = input().split(', ')

x = y = 0
mx, my = 1, 0

for i in moves:
    j = int(i[1:])
    i = i[0]
    if i == 'R':
        mx, my = my, -mx
    else:
        mx, my = -my, mx
    x += mx * j
    y += my * j

print(abs(x) + abs(y))
