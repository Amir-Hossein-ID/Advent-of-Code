n = int(input())

a = {(0,0): 1}

last = (0,0)
lastloc = 1
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
curdir = 0
curs = 3

while True:
    if lastloc == curs * curs:
        curs += 2
        # curdir += 1
        # curdir %= len(dirs)
    newloc = (last[0] + dirs[curdir][0], last[1] + dirs[curdir][1])
    ans = 0
    for i, j in [(1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, 1)]:
        ans += a.get((newloc[0] + i, newloc[1] + j), 0)
    a[newloc] = ans
    if ans > n:
        print(ans)
        break
    
    last = newloc
    lastloc += 1
    if lastloc in (curs * curs - curs + 1, curs * curs - 2 * (curs - 1), curs * curs - 3 * (curs - 1), (curs-2) ** 2 + 1):
        curdir += 1
        curdir %= len(dirs)
