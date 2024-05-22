dists = {}

for i in range(28): # no of inputs
    f, ans = input().split(' = ')
    fr, to = f.split(' to ')
    if fr not in dists:
        dists[fr] = {to: int(ans)}
    else:
        dists[fr][to] = int(ans)
    
    if to not in dists:
        dists[to] = {fr: int(ans)}
    else:
        dists[to][fr] = int(ans)

ans = -1

for current in dists:
    myans = 0
    visited = [current]

    while len(visited) != len(dists):
        where = sorted(dists[current], key=lambda x: (x in visited, dists[current][x]))
        visited.append(where[0])
        myans += dists[current][where[0]]
        current = where[0]
    
    if myans < ans or ans == -1:
        ans = myans

print(ans)
