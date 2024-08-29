moves = input().split(', ')

x = y = 0
mx, my = 0, 1
visited = set([(x, y)])

for i in moves:
    if i[0] == 'R':
        mx, my = my, -mx
    else:
        mx, my = -my, mx
    
    for p in range(int(i[1:])):
        x += mx
        y += my
        if (x, y) in visited:
            break
        visited.add((x, y))
    else:
        continue
    break

print(abs(x) + abs(y))
