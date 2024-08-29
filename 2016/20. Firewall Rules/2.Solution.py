ranges = []

for i in range(1104): # no of lines of input
    s, e = map(int, input().split('-'))
    ranges.append((s, e))

ranges.sort()
cur = 0
ans = 0

for i in ranges:
    if i[0] <= cur:
        cur = max(cur, i[1]+1)
    else:
        ans += i[0] - cur
        cur = max(cur, i[1]+1)

ans += 2 ** 32 - cur

print(ans)
